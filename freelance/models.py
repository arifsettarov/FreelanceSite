from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Work(models.Model):
    class Meta:
        verbose_name="Под-обл. деятельности"
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200, verbose_name="Название")

class Region(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200, verbose_name="Название")

class Orders(models.Model):
    class Meta:
        db_table="Orders"
        verbose_name="Заказы"
    def __str__(self):
        return str(self.id)
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    name = models.CharField(max_length=50, verbose_name="Имя")
    type = models.ForeignKey(Work, verbose_name="Категория")
    region = models.ForeignKey(Region, verbose_name="Регион", default=None)
    telephone = models.CharField(max_length=20, verbose_name="Телефон")
    description = models.TextField(verbose_name="Описание")
    price_start = models.IntegerField(default=0,verbose_name="Начальная цена")
    price_end = models.IntegerField(default=0,verbose_name="Конечная цена")
    date_time = models.CharField(max_length=100,default="Не важно", verbose_name="Дата и время")
    mailed = models.NullBooleanField(default=0)
class Workers(models.Model):
    class Meta:
        db_table="Workers"
        verbose_name="Соискатели"
    def __str__(self):
        return self.surname+" "+self.name
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    name = models.CharField(max_length=50, verbose_name="Имя")
    email = models.EmailField(verbose_name="E-mail")
    telephone = models.CharField(max_length=20, verbose_name="Телефон")
    SNILS = models.IntegerField(verbose_name="СНИЛС")
    password = models.CharField(max_length=100, verbose_name="Пароль")
    type = models.ManyToManyField(Work)
    region = models.ManyToManyField(Region, verbose_name="Регион")

class User_DATA(models.Model):
    email = models.EmailField(verbose_name="E-mail")
    password = models.CharField(max_length=100, verbose_name="Пароль")
    user_id = models.IntegerField()
