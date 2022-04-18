from django.contrib import admin

from relay_control.models import RelayBoardPinout, RelayBoardStatus


# Register your models here.
class RelayBoardPinoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pump_pin', 'mains_pin', 'byp_pin']
    readonly_fields = ['id']

    class Meta:
        model = RelayBoardPinout


admin.site.register(RelayBoardPinout, RelayBoardPinoutAdmin)


class RelayBoardStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pump_pin_state', 'mains_pin_state', 'byp_pin_state']
    readonly_fields = ['id']

    class Meta:
        model = RelayBoardStatus


admin.site.register(RelayBoardStatus, RelayBoardStatusAdmin)
