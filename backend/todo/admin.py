from django.contrib import admin
from .models import ToDo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')

# Register your models here.

admin.site.register(ToDo, TodoAdmin)

# admin.site.register(ToDo)