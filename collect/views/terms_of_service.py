from django.shortcuts import render


def index(request):
    return render(request, "collect/pages/terms-of-service.html")
