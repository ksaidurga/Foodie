from django.contrib import admin
from .models import Category, SubCategory, Product,ProductImage

admin.site.register(Category)
admin.site.register(SubCategory)
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1 
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
admin.site.register(Product,ProductAdmin)

