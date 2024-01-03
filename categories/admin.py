from django.contrib import admin

# Register your models here.
from .import models
# admin.site.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']

admin.site.register(models.Category, CategoryAdmin)