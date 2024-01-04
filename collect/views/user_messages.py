from django.shortcuts import render


def index(request, username):
    return render(request, "collect/user_messages.html")
