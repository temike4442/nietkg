from django import forms
from .models import Ad,Images

class AddForm(forms.ModelForm):

    class Meta:
        model=Ad
        fields=('title','content','category','number','name','region','address','price','valute')
        widgets={
            'title': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),'content': forms.Textarea(
                attrs={
                    'class':'form-control'
                }
            ),'category': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),'region': forms.Select(
                attrs={
                    'class':'form-control'
                }),
            'address': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),'name': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),'number': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

        }

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model=Images
        fields=('image',)