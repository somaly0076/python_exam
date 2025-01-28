from django.db import models

# Create your models here.
class CategoryTB(models.Model):
    name = models.CharField(max_length=50)

class ProductTB(models.Model):
    name =  models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    price = models.FloatField()
    Cat_id = models.ForeignKey(CategoryTB,related_name='products',on_delete= models.CASCADE)

