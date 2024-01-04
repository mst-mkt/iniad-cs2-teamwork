from django.contrib.auth.decorators import login_required
from django.db import models
from django.shortcuts import redirect

from collect.models import CustomUser, Friend


@login_required
def index(request, username):
    if request.user.username == username:
        return redirect("index")
    user = CustomUser.objects.get(username=username)
    is_friend = Friend.objects.filter(
        models.Q(user1_id=user.id, user2_id=request.user.id)
        | models.Q(user1_id=request.user.id, user2_id=user.id)
    ).exists()

    if not is_friend:
        Friend.objects.create(
            user1_id=request.user.id, user2_id=user.id, is_approved=False
        )

    return redirect("friends")


@login_required
def accept(request, username):
    user = CustomUser.objects.get(username=username)
    friend = Friend.objects.get(user1_id=user.id, user2_id=request.user.id)
    friend.is_approved = True
    friend.save()
    return redirect("friends")


@login_required
def reject(request, username):
    user = CustomUser.objects.get(username=username)
    friend = Friend.objects.get(user1_id=user.id, user2_id=request.user.id)
    friend.delete()
    return redirect("friends")


@login_required
def cancel(request, username):
    user = CustomUser.objects.get(username=username)
    friend = Friend.objects.get(user1_id=request.user.id, user2_id=user.id)
    friend.delete()
    return redirect("friends")
