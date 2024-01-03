from django.contrib.auth.views import LogoutView
from django.urls import path

import collect.views.friends as friends
import collect.views.login as login
import collect.views.messages as messages
import collect.views.notifications as notifications
import collect.views.settings as settings
import collect.views.signup as signup
import collect.views.top as top

urlpatterns = [
    path("", top.index, name="index"),
    path("signup/", signup.SignUpView.as_view(), name="signup"),
    path("login/", login.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("friends/", friends.index, name="friends"),
    path("notifications/", notifications.index, name="notifications"),
    path("messages/", messages.index, name="messages"),
    path("settings/", settings.index, name="settings"),
]
