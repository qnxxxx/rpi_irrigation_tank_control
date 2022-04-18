from django.contrib import admin
from core.models import BoardInitStatus, AutomaticMode


# Register your models here.
class BoardInitStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'init_state']
    readonly_fields = ['id']

    class Meta:
        model = BoardInitStatus


admin.site.register(BoardInitStatus, BoardInitStatusAdmin)


class AutomaticModeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'automatic_mode_enabled']
    readonly_fields = ['id']

    class Meta:
        model = AutomaticMode


admin.site.register(AutomaticMode, AutomaticModeAdmin)
