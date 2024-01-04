from django.contrib.auth.views import LogoutView
from django.urls import path

import collect.views.edit_profile as edit_profile
import collect.views.friends as friends
import collect.views.login as login
import collect.views.messages as messages
import collect.views.user_messages as user_messages
import collect.views.notifications as notifications
import collect.views.request as request
import collect.views.settings as settings
import collect.views.signup as signup
import collect.views.top as top
import collect.views.user as user

urlpatterns = [
    path("", top.index, name="index"),
    path("signup/", signup.SignUpView.as_view(), name="signup"),
    path("login/", login.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("friends/", friends.index, name="friends"),
    path("notifications/", notifications.index, name="notifications"),
    path("messages/", messages.index, name="messages"),
    path("messages/<str:username>", user_messages.index, name="user_messages"),
    path("settings/", settings.index, name="settings"),
    path("edit-profile/", edit_profile.edit_profile, name="edit-profile"),
    path("users/<str:username>/", user.index, name="user"),
    path("users/<str:username>/request/", request.index, name="request"),
    path("users/<str:username>/request/accept/", request.accept, name="accept"),
    path("users/<str:username>/request/reject/", request.reject, name="reject"),
    path("users/<str:username>/request/cancel/", request.cancel, name="cancel"),
]
