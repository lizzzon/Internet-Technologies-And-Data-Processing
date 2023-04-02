from django.views.generic import ListView


class MainPage(ListView):
    template_name = 'main.html'