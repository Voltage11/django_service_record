
from django.urls import path
from app.service.views.index import index


app_name = 'service'


urlpatterns = [
    path('auth/login', index, name='index'),
]
