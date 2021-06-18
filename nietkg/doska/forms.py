from django import forms
from .models import Ad,Images

class AddForm(forms.ModelForm):

    class Meta:
        model=Ad
        fields=('title','content','category','number','name','region','address','price','valute')
        widgets={

        }

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model=Images
        fields=('image',)