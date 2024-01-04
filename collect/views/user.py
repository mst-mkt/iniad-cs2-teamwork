from django.contrib.auth.decorators import login_required
from django.db import models
from django.shortcuts import redirect, render

from collect.models import CustomUser, Friend


@login_required
def index(request, username):
    if request.user.username == username:
        return redirect("index")
    user = CustomUser.objects.get(username=username)
    is_friend = Friend.objects.filter(
        models.Q(user1_id=user.id, user2_id=request.user.id, is_approved=True)
        | models.Q(user1_id=request.user.id, user2_id=user.id, is_approved=True)
    ).exists()
    context = {"user": user, "is_friend": is_friend}
    return render(request, "collect/gages/user.html", context)
