from django.contrib import admin
from .models import Person, Category


admin.site.register(Person)
admin.site.register(Category)