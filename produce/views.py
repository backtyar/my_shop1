from rest_framework import generics, filters
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from .models import Product, Category, Order, User
from .serializers import ProductSerializers, UserSerializers, CategorySerializers, OrderSerializers
from .permissions import CustomPermissions, CustomDetailPermissions


class ProductView(generics.ListAPIView):
    serializer_class = ProductSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['price']


    def get_queryset(self):
        return Product.objects.filter(available=True)


class CreateProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class DetailProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers






class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers



class DetailCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [permissions.IsAdminUser, ]


class OrderView(generics.ListAPIView):
    serializer_class = OrderSerializers
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers




class DetailUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    multiple_lookup_fields = ['username', 'password']

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj
    






