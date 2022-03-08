from django.contrib import admin
from helpers.caching_paginator import CachingPaginator

from water_level.models import SonarPinout, SampleMeasurement, TankSize, WaterLevel, MeasurementsInterval

# Register your models here.


class SampleMeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'sample_size', 'sample_wait', 'temperature']
    readonly_fields = ['id']

    class Meta:
        model = SampleMeasurement


admin.site.register(SampleMeasurement, SampleMeasurementAdmin)


class SonarPinoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'trigger_pin', 'echo_pin', 'failsafe_pin']
    readonly_fields = ['id']

    class Meta:
        model = SonarPinout


admin.site.register(SonarPinout, SonarPinoutAdmin)


class TankSizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'length', 'width', 'depth']
    readonly_fields = ['id']

    class Meta:
        model = TankSize


admin.site.register(TankSize, TankSizeAdmin)


class WaterLevelAdmin(admin.ModelAdmin):
    list_display = ['id', 'timestamp', 'water_level', 'volume_m3', 'volume_l', 'status_message', 'failsafe_status']
    search_fields = ['id', 'timestamp', 'water_level', 'volume_m3', 'volume_l', 'status_message', 'failsafe_status']
    readonly_fields = ['id', 'timestamp', 'water_level', 'volume_m3', 'volume_l', 'status_message', 'failsafe_status']

    show_full_result_count = False
    paginator = CachingPaginator

    class Meta:
        model = WaterLevel


admin.site.register(WaterLevel, WaterLevelAdmin)


class MeasurementsIntervalAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'interval']
    readonly_fields = ['id']

    class Meta:
        model = MeasurementsInterval


admin.site.register(MeasurementsInterval, MeasurementsIntervalAdmin)
