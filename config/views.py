from django.shortcuts import render


def terms_of_service(request):
    return render(request, "collect/terms-of-service.html")


def policy(request):
    return render(request, "collect/policy.html")
