from django.urls import path

import collect.views.top as top

urlpatterns = [
    path("", top.index, name="index"),
]
