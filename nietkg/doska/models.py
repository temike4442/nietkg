from django.db import models

class Category(models.Model):
    title=models.CharField('Имя категории',max_length=100,null=False,blank=False)
    parent=models.ForeignKey('self',on_delete=models.SET_NULL,null=True)
    url=models.SlugField(max_length=100,unique=True)
    icon=models.ImageField(upload_to='icons/',null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

class Ad(models.Model):
    title=models.CharField('Заголовок',max_length=150,null=False,blank=False)
    content=models.TextField('Описание',max_length=500)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=False,verbose_name='Категория')
    number=models.CharField('Тел. номер',null=False,blank=False,max_length=50)
    name=models.CharField('Имя',max_length=100)
    price=models.PositiveIntegerField('Цена',help_text='0 = Договорная')
    valute=models.ForeignKey('Valute',on_delete=models.SET_NULL,null=True,verbose_name='Валюта')
    image=models.ImageField(blank=True)
    is_active=models.BooleanField('Активация',default=False)
    is_vip=models.BooleanField('Статус VIP',default=False)
    date=models.DateTimeField('Дата',auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Обьявление'
        verbose_name_plural='Обьявлении'

class Images(models.Model):
    image=models.ImageField('Изображение',upload_to='upload_images/')
    ad=models.ForeignKey(Ad,on_delete=models.CASCADE)

    class Meta:
        verbose_name='Фото'
        verbose_name_plural='Фото'

class Valute(models.Model):
    title=models.CharField('Валюта',max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'