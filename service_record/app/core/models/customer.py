import uuid

from django.db import models

from app.users.models import CustomUser


class Customer(models.Model):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField('Наименование', max_length=255)
    phone = models.CharField('Телефон', max_length=255, null=True, blank=True)
    email = models.CharField('Email', max_length=255, null=True, blank=True)
    is_active = models.BooleanField('Активный', default=True)
    date_birth = models.DateField('Дата рождения', null=True, blank=True)
    address = models.TextField('Адрес', null=True, blank=True)
    comment = models.TextField('Комментарий', null=True, blank=True)
    create_at = models.DateTimeField('Дата создания', auto_now_add=True)
    update_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        db_table = 'customer'
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name