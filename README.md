Realtime irrigation tank control system on RaspberryPi, created with Django + Channels + Postgresql.

Features:
  1. Automatic and manual modes of operation.
  2. Realtime gauge for the water's level and quantity in the tank.
  3. Water level history graph.
  4. Control panel with realtime pumps/valves relay control and feedback.
  5. Authentication system defining user roles (viewers, operators and administrators).
  6. Chat system for communication between users.
  7. Notification system.
  8. Alarm system for critical water levels (high/low), sensor malfunctions, failsafe events.
  9. RPi pin settings, Measurement settings and Tank size are editable through the admin panel.
  10. !!! PERHAPS ONE DAY... !!! Android app or HASS.IO integration. Maybe both...?!?

Hardware:
  1. RaspberryPi 3 Model B v.1.2
  2. HC-SR04 Ultrasonic Sensor
  3. 3 Channel Relay Module With Opto-coupler Isolation Compatible 3.3V 5V Signal High-voltage Relay
  4. Failsafe - Push Button Momentary Switch

Software:
  1. OS - Raspberry Pi OS with desktop and recommended software

    Release date: January 28th 2022
    System: 32-bit
    Kernel version: 5.10
    Debian version: 11 (bullseye)

  2. Django + Channels + Celery
  3. Nginx
  4. Postgresql
  5. Gunicorn
  6. Daphne
  7. Redis

Chat system adapted from here: https://github.com/mitchtabian/Codingwithmitch-Chat

Current State ~50% Ready.
