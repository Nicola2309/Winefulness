from django import forms
from products.widgets import CustomClearableFileInput
from .models import Winemakers


class WinemakersForm(forms.ModelForm):

    class Meta:
        model = Winemakers
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
