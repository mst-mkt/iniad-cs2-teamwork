from io import BytesIO

import qrcode
import qrcode.image.svg
from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        context = {
            "user": request.user,
        }
        return render(request, "collect/index.html", context)
    else:
        return redirect("login")
