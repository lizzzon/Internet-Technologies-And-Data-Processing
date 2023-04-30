from django.urls import path
from apps.main.views import MainPage

urlpatterns = [
    path('', MainPage.as_view(), name='main')
]