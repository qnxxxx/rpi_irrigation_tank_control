from django.contrib import admin
from helpers.caching_paginator import CachingPaginator

from water_level.models import SonarPinout, SampleMeasurementSettings, TankSize, WaterLevel

# Register your models here.


class SampleMeasurementSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'sample_size', 'sample_wait', 'temperature', 'measurements_interval']
    readonly_fields = ['id']

    class Meta:
        model = SampleMeasurementSettings


admin.site.register(SampleMeasurementSettings, SampleMeasurementSettingsAdmin)


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
    list_display = ['id', 'timestamp', 'distance', 'volume_m3', 'volume_l', 'status', 'failsafe_engaged']
    search_fields = ['id', 'distance', 'volume_m3', 'volume_l', 'timestamp', 'status', 'failsafe_engaged']
    readonly_fields = ['id', 'distance', 'volume_m3', 'volume_l', 'timestamp', 'status', 'failsafe_engaged']

    show_full_result_count = False
    paginator = CachingPaginator

    class Meta:
        model = WaterLevel


admin.site.register(WaterLevel, WaterLevelAdmin)
