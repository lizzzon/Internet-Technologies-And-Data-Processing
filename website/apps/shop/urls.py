from django.urls import path
from apps.shop.views import ShopPage

urlpatterns = [
    path('shop/', ShopPage.as_view(), name='shop')
]