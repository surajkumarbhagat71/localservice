from django import forms
from  .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class PorsonForm(forms.ModelForm):
    class Meta:
        model = Porson
        exclude = ('category',)

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'

