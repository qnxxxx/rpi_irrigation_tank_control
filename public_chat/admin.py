from django.contrib import admin
from helpers.caching_paginator import CachingPaginator

from public_chat.models import PublicChatRoom, PublicRoomChatMessage


class PublicChatRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['id', 'title']
    readonly_fields = ['id']

    class Meta:
        model = PublicChatRoom


admin.site.register(PublicChatRoom, PublicChatRoomAdmin)


class PublicRoomChatMessageAdmin(admin.ModelAdmin):
    list_filter = ['room', 'user', 'timestamp']
    list_display = ['room', 'user', 'content', 'timestamp']
    search_fields = ['room__title', 'user__username', 'content']
    readonly_fields = ['id', 'user', 'room', 'timestamp']

    show_full_result_count = False
    paginator = CachingPaginator

    class Meta:
        model = PublicRoomChatMessage


admin.site.register(PublicRoomChatMessage, PublicRoomChatMessageAdmin)
