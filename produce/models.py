from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100,)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


# class Product(models.Model):
#     category = models.ForeignKey(Category, related_name='products')
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#
#
#     class Meta:
#         verbose_name = 'Продукт'
#         verbose_name_plural = 'Продукты'
#
#
#     def __str__(self):
#         return self.name
#
#
#
#
# class Order(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     address = models.CharField(max_length=250)
#     postal_code = models.CharField(max_length=20)
#     city = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     paid = models.BooleanField(default=False)
#
#     class Meta:
#         verbose_name = 'Заказ'
#         verbose_name_plural = 'Заказы'
#
#
#     def get_total_cost(self):
#         return sum(item.get_cost() for item in self.items.all())
#
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items')
#     product = models.ForeignKey(Product, related_name='order_items')
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)
#
#     def __str__(self):
#         return
#


