from django.urls import path
from apps.authentication.views import AuthPage

urlpatterns = [
    path('auth/', AuthPage.as_view(), name='auth')
]