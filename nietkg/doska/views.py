from django.core import serializers
from django.http import  JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *
from .forms import AddForm

class HomeView(ListView):
    model = Ad
    queryset = Ad.objects.filter(is_active=True)
    template_name = 'index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context=super(HomeView, self).get_context_data()
        context['category_list']=Category.objects.exclude(icon__isnull=True).exclude(icon__exact='')
        context['regions']=Region.objects.exclude(is_active=False)
        context['storie_list']=Story.objects.all()[:10]
        return context

def add_new(request):
    if request.method=='POST':
        form=AddForm(request.POST)
        if form.is_valid():
            valid_form=form.save()
            for image in request.FILES.getlist('images'):
                Images.objects.create(image=image,ad_id=valid_form.pk,)
            Trigger.objects.create(title=f'Обьявление №{valid_form.pk} отправлено на сервер.')
        return redirect('success',ad_id=valid_form.pk)
    else:
        form=AddForm(initial={'valute':1})
    return render(request,'add_post.html',{'form':form})

def success_view(request,ad_id):
    return render(request,'success.html',{'ad_id':ad_id})

class SuccessView(ListView):
    model = Ad
    template_name = 'success.html'

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_id')
        print(f'this id {ad_id}')
        return ad_id

def story_view(id):
    story_object = Story.objects.get(pk=id)
    story_object_items = StoryItem.objects.filter(story=story_object)
    story_object_list = serializers.serialize('json',[story_object,])
    story_object_items_list = serializers.serialize('json',story_object_items)
    return JsonResponse({'story_object_list':story_object_list,'story_object_items_list':story_object_items_list},safe=False,status=200)

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
        context['category_list'] = Category.objects.exclude(icon__isnull=True).exclude(icon__exact='')
        context['regions'] = Region.objects.exclude(is_active=False)
        return context

class AdSearchView(ListView):
    model = Ad
    template_name = 'search.html'
    paginate_by = 10
    context_object_name = 'result_list'
    result_count = 0

    def get_queryset(self):
        search_text=self.request.GET.get("search_text")
        region=self.request.GET.get("region")
        global result_count

        if region!='' and search_text=='' :
            result_count = Ad.objects.filter(region=region).count()
            return Ad.objects.filter(
                region=region
            )[:500]

        if region!='' and search_text!='' :
            result_count = Ad.objects.filter(region=region,title__icontains=search_text).count()
            return Ad.objects.filter(
                region=region,
                title__icontains=search_text
            )[:500]

        if region=='' and search_text!='' :
            result_count = Ad.objects.filter(title__icontains=search_text).count()
            return Ad.objects.filter(
                title__icontains=search_text
            )[:500]

        if region=='' and search_text=='' :
            result_count = 500
            return Ad.objects.all()[:500]

    def get_context_data(self, **kwargs):
        global result_count
        context=super(AdSearchView, self).get_context_data()
        context['category_list'] = Category.objects.exclude(icon__isnull=True).exclude(icon__exact='')
        context['regions'] = Region.objects.exclude(is_active=False)
        context['region_context']=self.request.GET.get("region")
        context['search_text']=self.request.GET.get("search_text")
        context['result_count']=result_count
        return context

class AdCategoryView(ListView):
    model = Ad
    template_name = 'category.html'
    context_object_name = 'ad_list'
    paginate_by = 10

    def get_queryset(self):
        return Ad.objects.filter(category=self.kwargs.get('pk'))[:100]

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.exclude(icon__isnull=True).exclude(icon__exact='')
        context['regions'] = Region.objects.exclude(is_active=False)
        context['storie_list'] = Story.objects.filter(story_category=self.kwargs.get('pk'))
        context['category']= self.kwargs.get('pk')
        pk = self.kwargs.get('pk')
        context['category_title']= Category.objects.get(pk=pk)
        return context
