from django.db import models

# Create your models here.
class CategoryTB(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class ProductTB(models.Model):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=50)
    image = models.ImageField(upload_to='crud_api/static/img',blank=True, null= True)
    price = models.FloatField()
    Cat_id = models.ForeignKey(CategoryTB,related_name='products',on_delete= models.CASCADE)

