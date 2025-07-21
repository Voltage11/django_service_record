from django.urls import path
from app.core.views.index import index
from app.core.views.service import service_list, service_create, service_update, service_delete


app_name = 'users'

urlpatterns = [
    path('service/list', service_list, name='service_list'),
    path('service/create', service_create, name='service_create'),
    path('service/update/<uuid:pk>', service_update, name='service_update'),
    path('service/delete/<uuid:pk>', service_delete, name='service_delete'),
    path('', index, name='index'),
]