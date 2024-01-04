from io import BytesIO

import qrcode
import qrcode.image.svg
from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        factory = qrcode.image.svg.SvgPathImage
        img = qrcode.make(
            f"http://localhost:8000/users/{request.user.username}",
            image_factory=factory,
            box_size=24,
        )
        stream = BytesIO()
        img.save(stream)
        svg = stream.getvalue().decode()
        context = {
            "user": request.user,
            "svg": svg,
        }
        return render(request, "collect/pages/index.html", context)
    else:
        return redirect("login")
