from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Table(models.Model):
    table = models.CharField(max_length=128, verbose_name = 'Стол')


    class Meta:
        #managed = False
        db_table = 'Table'
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'
    
    def __str__(self):
        return f'{self.table}'
    


class booking(models.Model):
    date = models.DateTimeField(default=timezone.now, verbose_name = 'Дата cоздание заявки')
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name = 'Заказчик') 
    table_booking = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True, verbose_name = 'Выберите стол')
    description = models.TextField('Комментарий к бронированию')
    date_booking = models.DateTimeField('Дата записи')


    class Meta:
        #managed = False
        db_table = 'booking'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'№{self.id} Зал.{self.table_booking} Дата {self.date}'



class News(models.Model):
    date = models.DateTimeField(default=timezone.now, verbose_name = 'Дата cоздание новости')
    title = models.TextField('Название новости')
    description = models.TextField('Новостной текс')
    image = models.ImageField(null=True, blank=True, upload_to="image/")
    
    class Meta:
        #managed = False
        db_table = 'News'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Menu(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название блюда')
    image = models.ImageField(null=True, blank=True, upload_to="menu/")
    content = models.TextField('Состав')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Menu'
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'