from django.forms import ModelForm
from app.core.models import Service

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'comment', 'price', 'is_active']

