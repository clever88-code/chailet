# Generated by Django 4.2.6 on 2023-11-20 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelTable(
            name='news',
            table='News',
        ),
    ]