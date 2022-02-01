from django.urls import path
from Accounts.views import RegisterApi, LoginApi, ShowProducts, AddtoCart, BuyProduct



urlpatterns = [
    path('signUp/', RegisterApi.as_view() ,name='Customer_register_api'),
    path('login/', LoginApi.as_view(), name='Login_api'),
    path('showProduct/', ShowProducts.as_view(), name='show_Product_api'),
    path('AddtoCart/', AddtoCart.as_view(), name='Add_toCart_api'),
    path('BuyProduct/', BuyProduct.as_view(), name='Buy_api'),

]