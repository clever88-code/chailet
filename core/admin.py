from django.contrib import admin
from .models import booking, Table, News, Menu
# Register your models here.
admin.site.register(booking)
admin.site.register(Table)
admin.site.register(News)
admin.site.register(Menu)
