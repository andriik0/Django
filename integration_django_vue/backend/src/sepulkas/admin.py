from django.contrib import admin
from sepulkas.models import Sepulka
# Register your models here.

@admin.register(Sepulka)
class SepulkaAdmin(admin.ModelAdmin):
    fields = [
        'coefficient',
        'slug',
    ]

