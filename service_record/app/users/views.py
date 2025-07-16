from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import View
from .forms import CustomAuthenticationForm

class LoginView(View):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:index')  # замените 'home' на ваш URL
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:index')  # замените 'home' на ваш URL
        return render(request, self.template_name, {'form': form})

def logout_view(request):
    logout(request)
    return redirect('users:login')