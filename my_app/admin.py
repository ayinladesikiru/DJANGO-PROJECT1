from django.contrib import admin

# Register your models here.
from my_app.models import Book, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_published'
    list_display = ['title', 'price', 'isbn']
    list_editable = ['isbn']
    search_fields = ['title']
    list_filter = ['publisher', 'date_published']
    fields = ['title', 'isbn']


# admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
