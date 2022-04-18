from django.apps import AppConfig


class MiscConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from helpers.rpi_gpio_init import board_init

        init = board_init()
        init_state, init_message = init['init_state'], init['status_message']

        if init_state:
            print(f'RPI INIT STATUS: {init_message}')
        else:
            print(f'RPI INIT ERROR: {init_message}')
