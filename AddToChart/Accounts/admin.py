from django.contrib import admin
from Accounts.models import ProductsItem , AddtoCart, Buyitem, UserCart, Item_inCart
# Register your models here.

admin.site.register(ProductsItem)
admin.site.register(AddtoCart)
admin.site.register(Buyitem)
admin.site.register(UserCart)
admin.site.register(Item_inCart)