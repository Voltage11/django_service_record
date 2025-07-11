from django.db import models

class Service(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='services')
    name = models.CharField("Наименование", max_length=255)
    price = models.DecimalField("Цена", max_digits=15, decimal_places=2, default=0)
    comment = models.TextField("Комментарий", blank=True, null=True)
    is_active = models.BooleanField("Активен", default=True)
    updated_at = models.DateTimeField("Обновлен", auto_now=True)
    created_at = models.DateTimeField("Создан", auto_now_add=True)

    class Meta:
        db_table = "service"
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


