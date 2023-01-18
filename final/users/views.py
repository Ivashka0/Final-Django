from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreationForm

# Create your views here.


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('http://127.0.0.1:8000')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

def start(request):
    return render(request, 'index.html')


def account_menu(request):
    return render(request, 'account.html')


def sign_menu(request):
    return render(request, 'login.html')