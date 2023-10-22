from django.contrib import admin
from .models import Catergory, Course


class CatergoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


# Register your models here.
admin.site.register(Catergory, CatergoryAdmin)
admin.site.register(Course)

