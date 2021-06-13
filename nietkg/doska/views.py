from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import *


class HomeView(ListView):
    model = Ad
    template_name = 'index.html'

    def get_queryset(self):
        return Ad.objects.all()

    def get_context_data(self, **kwargs):
        context=super(HomeView, self).get_context_data()
        context['category_list']=Category.objects.all()
        context['regions']=Region.objects.all()
        return context