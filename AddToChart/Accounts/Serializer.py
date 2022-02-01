import uuid

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from Accounts.models import ProductsItem, AddtoCart, Buyitem


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ShowProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsItem
        fields = '__all__'


class AddtoCartSerializer(serializers.ModelSerializer):
    user = RegisterSerializer(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=ProductsItem.objects.all())

    class Meta:
        model = AddtoCart
        fields = ('user', 'product')


class getCartSerializer(serializers.ModelSerializer):
    product = ShowProductSerializer(read_only=True)

    class Meta:
        model = AddtoCart
        fields = ('product',)


class BuyItemSerializer(serializers.ModelSerializer):
    user = RegisterSerializer(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=ProductsItem.objects.all())

    class Meta:
        model = Buyitem
        fields = ('user', 'product', 'quantity')
        read_only_fields = ('cost',)


class AllBuyItemSerializer(serializers.ModelSerializer):
    product = ShowProductSerializer(read_only=True)

    class Meta:
        model = Buyitem
        fields = ('product', 'cost', 'quantity')
