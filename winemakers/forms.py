from django import forms
from products.widgets import CustomClearableFileInput
from .models import Winemakers, Comments


class WinemakersForm(forms.ModelForm):
    """
    Winemakers details form
    """
    class Meta:
        model = Winemakers
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment', ]
