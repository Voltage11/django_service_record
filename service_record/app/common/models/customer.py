from django.db import models
from .rating import Rating

class Customer(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='customers')
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    second_name = models.CharField('Отчество', max_length=50, null=True, blank=True)
    full_name = models.CharField('Полное имя', max_length=200, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=50, null=True, blank=True)
    date_birth = models.DateField('Дата рождения', null=True, blank=True)
    comment = models.TextField('Комментарий', null=True, blank=True)
    rating = models.ForeignKey(Rating, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField('Активен', default=True)

    class Meta:
        db_table = 'customer'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = f'{self.surname} {self.name} {self.second_name}'
        super().save(*args, **kwargs)