from django import forms
from products.models import Cart


class NumberForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']
        widgets = {
            'quantity': forms.TextInput(attrs={
                'type': 'range',
                'class': 'form-control',
                'inputmode': 'numeric'
            })
        }