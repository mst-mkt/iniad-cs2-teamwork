from django.shortcuts import render

from collect.models import Notification


def index(request):
    notifications = Notification.objects.order_by("-posted_at")
    context = {"notifications": notifications}
    return render(request, "collect/pages/notifications.html", context)
