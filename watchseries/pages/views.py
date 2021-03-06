from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Page



class TestePageView(ListView):
    model = Page
    template_name = 'teste.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class FavoritePageView(TemplateView):
    template_name = 'favoritos.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class MaidPageView(TemplateView):
    template_name = 'maid.html'


