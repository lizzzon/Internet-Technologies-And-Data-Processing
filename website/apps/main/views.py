from django.shortcuts import render
from django.views import View

from apps.main.services import ProductHandler


class MainPage(View):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
            'products': ProductHandler.get_products(),
        })
