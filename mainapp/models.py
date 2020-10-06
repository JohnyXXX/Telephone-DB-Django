from django.core.validators import MinLengthValidator
from django.db import models


class Phonebook(models.Model):
    phone = models.CharField(max_length=11, unique=True, validators=[MinLengthValidator(11)], verbose_name='Телефон')
    lastname = models.CharField(max_length=25, verbose_name='Фамилия')
    firstname = models.CharField(max_length=25, verbose_name='Имя')
    patronymic = models.CharField(max_length=25, verbose_name='Отчество')
    city = models.CharField(max_length=25, verbose_name='Город')
    street = models.CharField(max_length=25, verbose_name='Улица')
    house = models.CharField(max_length=5, verbose_name='Дом')
    apartment = models.CharField(max_length=5, blank=True, null=True, verbose_name='Квартира')
