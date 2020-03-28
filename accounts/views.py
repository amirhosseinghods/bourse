from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.views import auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .forms import UserCreationForm

class RegisterView(SuccessMessageMixin, View):
    view_data = {"page_name": 'ثبت نام', "is_rtl": True}

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {"form": form, "view": self.view_data})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')

            # user = authenticate(username = username, password = raw_password)
            # login(request, user)
            messages.success(request, 'شما با موفقیت ثبت نام کردید.')
            return redirect('login')
    
        print(form.error_messages)
        return render(request, 'registration/signup.html', {"form": form, "view": self.view_data})