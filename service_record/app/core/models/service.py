from django.db import models

from app.users.models import CustomUser


class Service(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField('Наименование', max_length=150)
    comment = models.TextField('Комментарий', blank=True, null=True)
    is_active = models.BooleanField('Активен', default=True)
    price = models.DecimalField('Цена', max_digits=50, decimal_places=2)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        db_table = 'service'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name