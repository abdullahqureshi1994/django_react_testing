from rest_framework.response import Response
from rest_framework.views import APIView

from Accounts.Serializer import RegisterSerializer, ShowProductSerializer, AddtoCartSerializer, getCartSerializer, \
    AllBuyItemSerializer, BuyItemSerializer
from Accounts.models import ProductsItem
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


class RegisterApi(APIView):
    serializers_class = RegisterSerializer

    # permission_classes = [IsAuthenticated,]
    def post(self, request, format=None):
        serializers = self.serializers_class(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            user.save()
            data = serializers.data
            # refresh = RefreshToken.for_user(data)
            responce_data = {
                # 'access_token': str(refresh.access_token),
                'user': data

            }
            return Response(responce_data, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class LoginApi(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        # user = authenticate(email=email, password=password)
        print(user)
        if user is None:
            raise AuthenticationFailed('User Not Found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')

        data = RegisterSerializer(user)

        refresh = RefreshToken.for_user(user)
        responce_data = {
            'access_token': str(refresh.access_token),
            'user': data.data
        }
        return Response(responce_data, status=status.HTTP_200_OK)


class ShowProducts(APIView):
    serializers_class = ShowProductSerializer

    def get(self, request, format=None):
        data = ProductsItem.objects.all()

        serialized = ShowProductSerializer(data, many=True)
        Serialized_data = serialized.data

        return Response(Serialized_data, status=status.HTTP_200_OK)


class AddtoCart(APIView):
    serializers_class = AddtoCartSerializer

    def post(self, request, format=None):
        data = request.data
        value = data['product']
        print(value)
        serializers = self.serializers_class(data=data)
        if serializers.is_valid():
            user = serializers.save(user=request.user)
            user.save()
            data = serializers.data
            responce_data = {
                'user': data
            }
            return Response(responce_data, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self, request, format=None):
        data = request.user.Add_to_Car.all()
        print(data)
        serializer = getCartSerializer(data, many=True)
        Serialized_data = serializer.data

        responce = {
            'data': Serialized_data
        }
        return Response(responce, status=status.HTTP_200_OK)


class BuyProduct(APIView):
    serializers_class = BuyItemSerializer

    def post(self, request, format=None):
        data = request.data
        id = data['product']
        quantity = data['quantity']
        print(id)
        print(quantity)

        serializers = self.serializers_class(data=data)
        if serializers.is_valid():
            product = ProductsItem.objects.filter(id=id)
            for i in product:
                i.Quanity = i.Quanity - quantity
                i.save()
                price = quantity * i.rate

            user = serializers.save(user=request.user, cost=price)
            user.save()

            data = serializers.data
            responce_data = {
                'user': data
            }
            return Response(responce_data, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self, request, format=None):
        data = request.user.Buy_Product.all()
        serializer = AllBuyItemSerializer(data, many=True)
        Serialized_data = serializer.data

        responce = {
            'data': Serialized_data
        }
        return Response(responce, status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     print(request.data)
    #     data = request.data
    #
    #     id = data['product']
    #     quantity = data['Quantity']
    #
    #     data = ProductsItem.objects.filter(id=id)
    #     print(data)
    #     value = 0
    #     for i in data:
    #         value = i.Quanity - quantity
    #         i.Quanity = value
    #         i.save()
    #
    #     val = ProductsItem.objects.filter(id=id)
    #     print(val)
    #     for j in val:
    #         print(j.Quanity)
    #
    #     return Response("responce", status=status.HTTP_200_OK)
