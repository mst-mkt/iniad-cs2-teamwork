from django.shortcuts import redirect, render

from ..forms import EditProfileForm


def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, "collect/pages/edit-profile.html", {"form": form})
