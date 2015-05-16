from django.conf.urls import include, url
import socketio.sdjango

urlpatterns = [
    url("^socket\.io", include(socketio.sdjango.urls)),
]