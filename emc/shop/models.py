from django.db import models


# Create your models here.
class Products(models.Model):
    objects = models.Manager()
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    Price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000)
    pub_date = models.DateField()
    image = models.FileField(blank=True)

    def __str__(self):
        return self.product_name


class PostImage(models.Model):
    objects = models.Manager()
    post = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='shop/img')

    def __str__(self):
        return self.post.product_name
