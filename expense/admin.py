from django.contrib import admin
from .import models
# Register your models here.
class db(admin.ModelAdmin):
    list_display=['months','name','amount','date']

admin.site.register(models.et,db)