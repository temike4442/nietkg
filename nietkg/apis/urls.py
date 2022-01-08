from django.urls import path,include
from .views import ListAd, DetailAd, CreateAd, CategoryAd, SearchAd, Categories, Regions, Valutes,Stories_Category, Stories, \
    Story_View

urlpatterns=[
    path('',ListAd.as_view()),
    path('<int:pk>/',DetailAd.as_view()),
    path('create/',CreateAd.as_view()),
    path('category/<int:id>/<int:region>/',CategoryAd.as_view()),
    path('search/<str:search_text>/<int:region>/<int:category>/',SearchAd.as_view()),
    path('category_list/',Categories.as_view()),
    path('region_list/',Regions.as_view()),
    path('story_list/',Stories.as_view()),
    path('story_list/<int:cat_id>',Stories_Category.as_view()),
    path('story/<int:id>',Story_View.as_view()),
    path('valute_list/',Valutes.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]