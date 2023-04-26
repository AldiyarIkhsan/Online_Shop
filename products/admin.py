from django.contrib import admin

# Register your models here.
from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'stripe_product_price_id', 'image', 'category')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('-name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0
