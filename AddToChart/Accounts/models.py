from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class ProductsItem(models.Model):
    Brand = (
        ('Local', 'Local'),
        ('Branded', 'Branded'),
        ('Imported', 'Imported'),
    )
    Name = models.CharField(max_length=1000, blank=True)
    Image = models.ImageField(upload_to="Product_Image/", null=True, blank=True)
    Quanity = models.IntegerField(blank=True)
    rate = models.IntegerField(blank=True)
    brand = models.CharField(max_length=255, choices=Brand)

    def __str__(self):
        return f"Product Name : {self.Name}"


class AddtoCart(models.Model):
    user = models.ForeignKey(User, related_name="Add_to_Car", on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(ProductsItem, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Uer Name : {self.user}   Product is : {self.product}"


class UserCart(models.Model):
    user = models.ForeignKey(User, related_name="User_cart", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Cart of User : {self.user}"


class Item_inCart(models.Model):
    cart = models.ForeignKey(UserCart, related_name="Cart_Item", on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(ProductsItem, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Uer Name : {self.cart.user}   Product is : {self.product} Quantity is: {self.quantity}"


class Buyitem(models.Model):
    user = models.ForeignKey(User, related_name="Buy_Product", on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(ProductsItem, on_delete=models.CASCADE, blank=True, null=True)
    cost = models.BigIntegerField(blank=True, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Uer Name : {self.user}   Product is : {self.product} Remaining is: {self.quantity} Cost is :{self.cost}"

# class AddtoCart(models.Model):
#     user = models.ForeignKey(User, related_name="Add_to_Car",on_delete=models.CASCADE, blank=True, null=True)
#     product = models.ManyToManyField(to=ProductsItem)
#
#     def __str__(self):
#         return f"Uer Name : {self.user}   Product is : {self.product}"
