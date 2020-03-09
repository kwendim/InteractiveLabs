from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import labs.routing


application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            labs.routing.websocket_urlpatterns
        )
    ),
})
