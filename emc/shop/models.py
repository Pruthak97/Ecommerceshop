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
    image = models.ImageField(upload_to="shop/img", default="")

    def __str__(self):
        return self.product_name


class Userlogin(models.Model):
    objects = models.Manager()
    user_name = models.AutoField
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name
