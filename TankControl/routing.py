from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path

from core.consumers import ModeConsumer
from notification.consumers import NotificationConsumer
from public_chat.consumers import PublicChatConsumer
from relay_control.consumers import RelayControlConsumer
from water_level.consumers import WaterLevelConsumer


application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path('mode/', ModeConsumer.as_asgi()),
                path('', NotificationConsumer.as_asgi()),
                path('public_chat/<room_id>/', PublicChatConsumer.as_asgi()),
                path('rb/', RelayControlConsumer.as_asgi()),
                path('wl/', WaterLevelConsumer.as_asgi()),

            ])
        )
    ),
})
