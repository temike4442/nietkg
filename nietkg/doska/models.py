from django.db import models
from django.urls import reverse


class Region(models.Model):
    title=models.CharField('Регион',max_length=50)
    is_active=models.BooleanField('Активация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

class Category(models.Model):
    title=models.CharField('Имя категории',max_length=100,null=False,blank=False)
    parent=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    url=models.SlugField(max_length=100,unique=True)
    icon=models.ImageField(upload_to='icons/',null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

class Ad(models.Model):
    title=models.CharField('Заголовок',max_length=150,null=False,blank=False)
    content=models.TextField('Описание',max_length=500,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=False,verbose_name='Категория')
    number=models.CharField('Тел. номер',null=False,blank=False,max_length=50)
    name=models.CharField('Имя',max_length=100,null=True,blank=True)
    region=models.ForeignKey(Region,on_delete=models.PROTECT,verbose_name='Регион',null=False,blank=False,default=None)
    address=models.CharField('Адрес',max_length=150,null=True,blank=True)
    price=models.PositiveIntegerField('Цена',help_text='0 = Договорная')
    valute=models.ForeignKey('Valute',on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Валюта')
    views=models.PositiveIntegerField('Просмотры',default=0)
    is_active=models.BooleanField('Активация',default=False)
    is_vip=models.BooleanField('Статус VIP',default=False)
    date=models.DateTimeField('Дата',auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ad_detail', kwargs={"pk": self.pk})

    class Meta:
        verbose_name='Обьявление'
        verbose_name_plural='Обьявлении'

class Images(models.Model):
    image=models.ImageField('Изображение',upload_to='upload_images/%Y/%m/%d/')
    ad=models.ForeignKey(Ad,on_delete=models.CASCADE,related_name='images')

    class Meta:
        verbose_name='Фото'
        verbose_name_plural='Фото'


    def __str__(self):
        return str(self.image)

class Valute(models.Model):
    title=models.CharField('Валюта',max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

class Story(models.Model):
    story_title = models.CharField('Заголовок', max_length=300, null=True, blank=True)
    story_date = models.DateTimeField(auto_now_add=True)
    story_category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)

class StoryItem(models.Model):
    story=models.ForeignKey(Story,on_delete=models.CASCADE)
    CHOICES=(
        ('mp4','video'),
        ('jpg','image'),
    )
    story_type=models.CharField(max_length=300, choices = CHOICES, null=False,blank=False)
    story_src=models.FileField('Ресурс',upload_to='stories/%Y/%m/%d/',null=False,blank=False)
