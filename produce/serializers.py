from rest_framework import serializers

from .models import Product, Category, Order, User


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        read_only = ['created', 'available']



class CategorySerializers(serializers.ModelSerializer):
    # product =

    class Meta:
        model = Category
        fields = '__all__'



class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['password'],
            validated_data['email']
        )
        return user


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'










