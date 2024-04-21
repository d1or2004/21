from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from product.models import Product
from .forms import RegistrationForm, LoginForm


class LandingPage(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'main/index.html', context)


class SignUpPageView(CreateView):
    form_class = RegistrationForm
    model = User
    success_url = 'login/'
    template_name = 'main/sign.html'


class LoginPageView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'main/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        username = form['username'].value()
        password = form['password'].value()
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('landing')

        return render(request, 'main/login.html', {'form': form})
