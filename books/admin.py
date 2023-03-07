from django.contrib import admin

# Register your models here.
from books.models import Books_model


class Books_modelmodeladmin(admin.ModelAdmin):
    list_display = ['Tittle', "id"]
    search_fields = ['Tittle', ]

    class Meta:
        model = Books_model


admin.site.register(Books_model, Books_modelmodeladmin)
