from django.forms import modelformset_factory
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from .models import *
from .forms import AddForm,ImageForm

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

def add_new(request):
    if request.method=='POST':
        form=AddForm(request.POST)
        if form.is_valid():
            valid_form=form.save()
            for image in request.FILES.getlist('images'):
                photo=Images(ad=valid_form,image=image)
                photo.save()
        return HttpResponseRedirect('/')
    else:
        form=AddForm()
    return render(request,'add_post.html',{'form':form})