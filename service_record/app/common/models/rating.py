from django.db import models

class Rating(models.Model):
    name = models.CharField('Наименование', max_length=100, unique=True)
    color = models.CharField('Цвет', max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'rating'
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return self.name