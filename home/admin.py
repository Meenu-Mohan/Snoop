from django.contrib import admin
from .models import Juvenile, Image


class ImageInline(admin.TabularInline):
    model = Image

class JuvenilesAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Juvenile, JuvenilesAdmin)

# Register your models here.
