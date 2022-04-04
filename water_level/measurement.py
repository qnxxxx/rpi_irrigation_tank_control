from __future__ import division

import time
import math

import RPi.GPIO as GPIO
from asgiref.sync import sync_to_async

from helpers.get_sonar_settings import TRIGGER_PIN, ECHO_PIN, FAILSAFE_PIN
from helpers.get_measurement_settings import SAMPLE_SIZE, SAMPLE_WAIT, TEMPERATURE
from helpers.get_tank_size import TANK_DEPTH


@sync_to_async
class Measurement:
    """
    Create a measurement using a HC-SR04 Ultrasonic Sensor connected to
    the GPIO pins of a Raspberry Pi.
    temperature=<Desired temperature in >
    """
    def __init__(self, gpio_mode=GPIO.BCM):
        self.trig_pin = TRIGGER_PIN
        self.echo_pin = ECHO_PIN
        self.failsafe_pin = FAILSAFE_PIN
        self.gpio_mode = gpio_mode
        self.result = {'water_level': -1.0, 'volume_m3': -1.0, 'volume_l': -1.0, 'tank_fill': -1.0,
                       'failsafe': False, 'status': ''}
        self.sonar_signal_on = 0
        self.sonar_signal_off = 0

    async def distance(self, sample_size=SAMPLE_SIZE, sample_wait=SAMPLE_WAIT, temperature=TEMPERATURE):
        """
        Return an error corrected rounded to the second decimal point
        distance, in cm, of an object adjusted for temperature in Celsius.
        The distance calculated is the median value of a sample of `sample_size` readings.
        Speed of readings is a result of two variables.  The sample_size
        per reading and the sample_wait (interval between individual samples).
        Example: To use a sample size of 5 instead of 11 will increase the
        speed of your reading but could increase variance in readings;
        value = sensor.Measurement(trig_pin, echo_pin)
        r = value.raw_distance(sample_size=5)
        Adjusting the interval between individual samples can also
        increase the speed of the reading.  Increasing the speed will also
        increase CPU usage.  Setting it too low will cause errors.  A default
        of sample_wait=0.1 is a good balance between speed and minimizing
        CPU usage.  It is also a safe setting that should not cause errors.
        e.g.
        r = value.raw_distance(sample_wait=0.03)
        """

        speed_of_sound = 331.3 * math.sqrt(1 + (temperature / 273.15))
        sample = []

        for _ in range(sample_size):
            GPIO.output(self.trig_pin, GPIO.LOW)
            time.sleep(sample_wait)
            GPIO.output(self.trig_pin, True)
            time.sleep(0.00001)
            GPIO.output(self.trig_pin, False)
            echo_status_counter = 1
            while GPIO.input(self.echo_pin) == 0:
                if echo_status_counter < 1000:
                    self.sonar_signal_off = time.time()
                    echo_status_counter += 1
                else:
                    self.result['status'] = 'Error: Echo pulse not received! Check the sonar health!'
                    return self.result
            # print(f'SONAR_SIGNAL_OFF: {self.sonar_signal_off}')
            while GPIO.input(self.echo_pin) == 1:
                self.sonar_signal_on = time.time()
            # print(f'SONAR_SIGNAL_ON: {self.sonar_signal_on}')
            time_passed = self.sonar_signal_on - self.sonar_signal_off
            distance_cm = time_passed * ((speed_of_sound * 100) / 2)
            sample.append(distance_cm)
        sorted_sample = sorted(sample)
        self.result['water_level'] = round(TANK_DEPTH - (sorted_sample[sample_size // 2]), 1)
        self.result['status'] = 'Success!'

        # Determine failsafe status
        if not GPIO.input(self.failsafe_pin):
            self.result['failsafe'] = True
            # print('button pressed')
        else:
            self.result['failsafe'] = False
            # print('button depressed')

        return self.result
