from .models import *

menu = [{"title": "Головна", "url_name": "main"},
        {"title": "Уроки", "url_name": "subjects"},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        context["menu"] = menu
