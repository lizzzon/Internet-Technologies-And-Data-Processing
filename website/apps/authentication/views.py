from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q
from apps.authentication.forms import RegisterForm, LoginForm
from django.contrib.auth.hashers import make_password, check_password


class AuthPage(View):
    template_name = 'auth.html'

    def get(self, request, *args, **kwargs):
        login_form = LoginForm()
        register_form = RegisterForm()

        return render(request, self.template_name, context={
            'login_form': login_form,
            'register_form': register_form,
        })

    def post(self, request, *args, **kwargs):
        logout(request)

        login_form = LoginForm(request.POST)
        register_form = RegisterForm(request.POST)
        try:
            if register_form.is_valid():
                print('REGISTER FORM')
                self._register(request, register_form)
            elif login_form.is_valid():
                print('LOGIN FORM')
                self._login(request, login_form)
            else:
                print(register_form.errors)
                print(login_form.errors)
                raise ValueError('form_errors')
        except ValueError as ex:
            print(ex)
        else:
            print('SUCCESS REDIRECT')
            return redirect('main')

        return render(request, self.template_name, context={
            'login_form': login_form,
            'register_form': register_form,
        })

    def _login(self, request, form: LoginForm):
        if not User.objects.filter(email=form.cleaned_data['email']).exists():
            raise ValueError('user_not_exists')

        user = User.objects.get(
            email=form.cleaned_data['email'],
        )

        if not check_password(
            form.cleaned_data['password'],
            user.password,
        ):
            raise ValueError('invalid_password')

        login(request, user)
        print('LOGIN SUCCESS')

    def _register(self, request, form: RegisterForm):
        if User.objects.filter(Q(email=form.cleaned_data['email']) | Q(username=form.cleaned_data['name'])).exists():
            raise ValueError('user_exists')

        user = User(
            email=form.cleaned_data['email'],
            username=form.cleaned_data['name'],
            password=make_password(form.cleaned_data['password']),
        )

        user.save()

        print('REGISTER SUCCESS GO TO LOGIN')
