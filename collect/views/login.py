from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

from ..forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "collect/pages/login.html"
    success_url = reverse_lazy("index")

    def get_success_url(self):
        return self.success_url or super().get_success_url()
