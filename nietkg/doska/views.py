from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import *
from .forms import AddForm,ImageForm

class HomeView(ListView):
    model = Ad
    queryset = Ad.objects.filter(is_active=True)
    template_name = 'index.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context=super(HomeView, self).get_context_data()
        context['category_list']=Category.objects.all()
        context['ad_vip_list']=Ad.objects.filter(is_vip=True)
        context['regions']=Region.objects.all()
        return context

def add_new(request):
    if request.method=='POST':
        form=AddForm(request.POST)
        if form.is_valid():
            valid_form=form.save()
            for image in request.FILES.getlist('images'):
                Images.objects.create(image=image,ad_id=valid_form.pk,)
        return redirect('/')
    else:
        form=AddForm()
    return render(request,'add_post.html',{'form':form})


class AdView(DetailView):
    model = Ad
    template_name = 'ad.html'

    def get_object(self, queryset=None):
        item=super(AdView, self).get_object(queryset)
        item.views+=1
        item.save()
        return item

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['regions'] = Region.objects.all()
        return context

class AdSearchView(ListView):
    model = Ad
    template_name = 'search.html'
    paginate_by = 20
    context_object_name = 'result_list'

    def get_queryset(self):
        search_text=self.request.GET.get("search_text")
        region=self.request.GET.get("region")

        if region!='' and search_text=='' :
            print('region!='' and search_text==''')
            return Ad.objects.filter(
                region=region
            )

        if region!='' and search_text!='' :
            print('region!='' and search_text!=')
            return Ad.objects.filter(
                region=region,
                title__icontains=search_text
            )

        if region=='' and search_text!='' :
            print('region=='' and search_text!=''')
            return Ad.objects.filter(
                title__icontains=search_text
            )

        if region=='' and search_text=='' :
            print('region=='' and search_text==')
            return Ad.objects.all()

    def get_context_data(self, **kwargs):
        context=super(AdSearchView, self).get_context_data()
        context['category_list']=Category.objects.all()
        context['regions']=Region.objects.all()
        context['region_context']=self.request.GET.get("region")
        print('region: '+self.request.GET.get("region"))
        context['search_text']=self.request.GET.get("search_text")
        return context

class AdCategoryView(ListView):
    model = Ad
    template_name = 'category.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['ad_list']=Ad.objects.filter(category=self.kwargs.get('pk'))
        context['category_list'] = Category.objects.all()
        context['regions'] = Region.objects.all()
        context['category']= self.kwargs.get('pk')
        return context

class AllCategories(ListView):
    model = Ad