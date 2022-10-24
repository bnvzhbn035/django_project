from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import RegisterUserForm
from .models import *
from .utils import *


# Create your views here.

def main(requests):
    response = render_to_string("site_project/index1.html")
    return HttpResponse(response)


def subjects(requests):
    response2 = render_to_string("site_project/index2.html")
    return HttpResponse(response2)

    if response2 == "/subjects/main":
        return HttpResponseRedirect(response)


def register(request):
    return HttpResponse("Реєстрація")


def login(request):
    return HttpResponse("Авторизація")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "site_project/register.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Реєстрація")
        return dict(list(context.items()) + list(c_def.items()))
