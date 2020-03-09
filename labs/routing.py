from django.urls import re_path

from . import terminal_consumers

websocket_urlpatterns = [
    re_path(r'ws/labs/(?P<lab_id>\w+)/$', terminal_consumers.TerminalConsumer),
]