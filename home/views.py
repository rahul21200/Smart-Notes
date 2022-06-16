from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

# def home(request):
#     # return HttpResponse("Hello, world!")
#     return render(request, 'home/welcome.html', {'today': datetime.today()})


class AuthorisedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorised.html'
    login_url = '/admin'
# @login_required(login_url='/admin')
# def authorised(request):
#     return render(request, 'home/authorised.html', {})
