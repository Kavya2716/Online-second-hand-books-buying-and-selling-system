from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=500, default='')
    image = models.ImageField(upload_to='uploads/products/')
    image_i = models.ImageField(upload_to='uploads/products/' , default='')
    image_b = models.ImageField(upload_to='uploads/products/' , default='')
    stock = models.IntegerField(default=100)
    author = models.CharField(max_length=50, default='Chetan Bhagat')
    page = models.IntegerField(default=200)
    publisher = models.CharField(max_length=500, default='Rupa Publications')
    language = models.CharField(max_length=500, default='English')
    edition = models.CharField(max_length=500,default='Febrauary 2018')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_products_by_id(ids):
        return  Product.objects.filter(id__in = ids)

    def reg(self):
        self.save()

    def __str__(self):
        return self.name