# Generated by Django 4.2.6 on 2023-11-20 07:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата cоздание новости')),
                ('title', models.TextField(verbose_name='Название новости')),
                ('description', models.TextField(verbose_name='Новостной текс')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
            ],
        ),
    ]