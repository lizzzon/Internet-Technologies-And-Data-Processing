from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.main.services import ProductHandler

class ShopPage(View):
    template_name = 'shop.html'

    @method_decorator(login_required(login_url='auth'))
    def get(self, request, *args, **kwargs):
        print(request.user)
        return render(request, self.template_name, context={
            'products': ProductHandler.get_products(),
        })