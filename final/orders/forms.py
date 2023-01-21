from django.forms import ModelForm, TextInput
from orders.models import CreditCard


class CreditCardForm(ModelForm):
    class Meta:
        model = CreditCard
        fields = ['name', 'credit_number', 'expiration', 'security_code']

        widgets = {
            "name": TextInput(attrs={
                'id': 'name',
                'placeholder': 'Name',
                'maxlength': 20
            }),
            "credit_number": TextInput(attrs={
                'id': 'cardnumber',
                'placeholder': 'Card Number',
                'inputmode': 'numeric'
            }),
            "expiration": TextInput(attrs={
                'id': 'expirationdate',
                'placeholder': 'Expiration (mm/yy)',
                'inputmode': 'numeric'
            }),
            "security_code": TextInput(attrs={
                'id': 'securitycode',
                'placeholder': 'Security Code',
                'inputmode': 'numeric'
            })
        }