from django.shortcuts import render


def index(request, username):
    return render(request, "collect/pages/user_messages.html")
