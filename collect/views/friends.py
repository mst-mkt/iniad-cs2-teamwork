from django.shortcuts import render

from collect.models import CustomUser, Friend


def index(request):
    friends_as_user1 = Friend.objects.filter(user1=request.user, is_approved=True)
    friends_as_user2 = Friend.objects.filter(user2=request.user, is_approved=True)
    friend_users = list(friends_as_user1.values_list("user2", flat=True)) + list(
        friends_as_user2.values_list("user1", flat=True)
    )
    friends = CustomUser.objects.filter(id__in=friend_users)
    context = {"friends": friends}
    return render(request, "collect/friends.html", context)
