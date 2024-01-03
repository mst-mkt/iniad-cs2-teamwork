from django.urls import path

import collect.views.friends as friends
import collect.views.messages as messages
import collect.views.notifications as notifications
import collect.views.settings as settings
import collect.views.top as top

urlpatterns = [
    path("", top.index, name="index"),
    path("friends/", friends.index, name="friends"),
    path("notifications/", notifications.index, name="notifications"),
    path("messages/", messages.index, name="messages"),
    path("settings/", settings.index, name="settings"),
]
