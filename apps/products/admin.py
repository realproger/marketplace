from django.contrib import admin
from apps.products.models import Product, ProductImage, Discount, ProductComment, FavouriteProduct, LikeProduct

# Register your models here.

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 3

class ProductDiscountAdmin(admin.TabularInline):
    model = Discount
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin, ProductDiscountAdmin]
    list_display = ('title', 'price')
    search_fields = ('title', 'price')
    ordering = ('-price',)
    list_per_page = 4

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductComment)
admin.site.register(FavouriteProduct)
admin.site.register(LikeProduct)

