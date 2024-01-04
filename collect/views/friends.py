from django.shortcuts import render

from collect.models import CustomUser, Friend


def index(request):
    friends_as_user1 = Friend.objects.filter(user1=request.user, is_approved=True)
    friends_as_user2 = Friend.objects.filter(user2=request.user, is_approved=True)
    friend_users = list(friends_as_user1.values_list("user2", flat=True)) + list(
        friends_as_user2.values_list("user1", flat=True)
    )
    friends = CustomUser.objects.filter(id__in=friend_users)

    friends_requests = Friend.objects.filter(user2=request.user, is_approved=False)
    friends_requests_users = list(friends_requests.values_list("user1", flat=True))
    friends_requests = CustomUser.objects.filter(id__in=friends_requests_users)

    friends_pending = Friend.objects.filter(user1=request.user, is_approved=False)
    friends_pending_users = list(friends_pending.values_list("user2", flat=True))
    friends_pending = CustomUser.objects.filter(id__in=friends_pending_users)

    context = {
        "friends": friends,
        "friends_requests": friends_requests,
        "friends_pending": friends_pending,
    }
    return render(request, "collect/pages/friends.html", context)
