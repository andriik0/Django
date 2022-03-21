from django.contrib import admin

from .models import Book
from .models import Review

class ReviewInline(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "author", "price",)


# Register your models here.
admin.site.register(Book, BookAdmin)
