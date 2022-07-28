from django.db import models


class Vehicle(models.Model):

    brand = models.CharField(verbose_name='Марка', max_length=200)
    model = models.CharField(verbose_name='Модель', max_length=200)
    price = models.IntegerField(verbose_name='Цена в рублях', null=True)
    power = models.IntegerField(verbose_name='Мощность двигателя')
    colour = models.CharField(verbose_name='Цвет', max_length=200)
    release_date = models.DateField(verbose_name='Дата выпуска')
    delivery_date = models.DateField(verbose_name='Дата поступления')
    sale_date = models.DateField(verbose_name='Дата продажи', default=None)

    def __str__(self):
        return self.model
