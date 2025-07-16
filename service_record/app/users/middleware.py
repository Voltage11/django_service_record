from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Исключаем страницу входа и статические файлы
        if not request.user.is_authenticated and request.path != reverse('users:login') and not request.path.startswith(settings.STATIC_URL):
            return redirect('users:login')
        return self.get_response(request)