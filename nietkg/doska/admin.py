from django.contrib import admin
from .models import *


class ImagesAdminInline(admin.TabularInline):
    list_display = ('image','ad')
    model = Images

class AdAdmin(admin.ModelAdmin):
    list_display = ('title','category','is_active','is_vip','date')
    list_display_links = ('title',)
    list_editable = ('category','is_active','is_vip')
    inlines =[ImagesAdminInline,]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','parent')
    prepopulated_fields = {"url": ("title",)}

class ValuteAdmin(admin.ModelAdmin):
    list_display = ('title',)

class RegionAdmin(admin.ModelAdmin):
    list_display = ('title','is_active')
    list_display_links = ('title',)

admin.site.register(Ad,AdAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Valute,ValuteAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Images)
