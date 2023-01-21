from django.shortcuts import render, redirect
from orders.models import *
from products.models import *
from orders.forms import CreditCardForm

# Create your views here.


def start(request):
    error = ''
    form1 = CreditCardForm()
    if request.user.is_authenticated:
        summ = 0
        context = Cart.objects.filter(user=request.user).values('price')
        for element in context:
            summ += element['price']
        if request.method == 'POST':
            form = CreditCardForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                _ = CreditCard.objects.get_or_create(
                    user=request.user,
                    name=form.cleaned_data['name'],
                    sum=summ,
                    credit_number=form.cleaned_data['credit_number'],
                    expiration=form.cleaned_data['expiration'],
                    security_code=form.cleaned_data['security_code'],
                    status='Processing'
                )
                return redirect('http://127.0.0.1:8000')
            else:
                error = 'Form was completed incorrectly'
        return render(request, 'pay.html', {'sum': summ, "form": form1, 'error': error})
    else:
        return render(request, 'closed.html')

