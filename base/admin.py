from django.contrib import admin
from .models import *
# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    model=ProductsModel
    list_display=['id','pname','pcategory','pimage']

admin.site.register(ProductsModel,ProductsAdmin)