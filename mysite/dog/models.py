from django.db import models

# Create your models here.
class AgilityClass(models.Model):
    def __str__(self):
        return self.agilityclass_name
    agilityclass_name = models.CharField(max_length=200)
    agilityclass_description = models.CharField(max_length=1000)
    agilityclass_price = models.FloatField()
    agilityclass_length = models.CharField(max_length=50)
    agilityclass_image = models.CharField(max_length=500, default="https://classroomclipart.com/image/static7/preview2/cartoon-dog-sitting-down-with-a-black-nose-outline-57221.jpg")
    agilityclass_week1 = models.CharField(max_length=10000, default="")
    agilityclass_week2 = models.CharField(max_length=10000, default="")
    agilityclass_week3 = models.CharField(max_length=10000, default="")
    agilityclass_week4 = models.CharField(max_length=10000, default="")
    agilityclass_week5 = models.CharField(max_length=10000, default="")
    agilityclass_week6 = models.CharField(max_length=10000, default="")


class NonAgilityClass(models.Model):
    def __str__(self):
        return self.nonagilityclass_name
    nonagilityclass_name = models.CharField(max_length=200)
    nonagilityclass_description = models.CharField(max_length=1000)
    nonagilityclass_price = models.FloatField()
    nonagilityclass_length = models.CharField(max_length=50)
    nonagilityclass_week1 = models.CharField(max_length=10000, null=True)
    nonagilityclass_image = models.CharField(max_length=500, default="https://classroomclipart.com/image/static7/preview2/cartoon-dog-sitting-down-with-a-black-nose-outline-57221.jpg")


class Product(models.Model):
    def __str__(self):
        return self.product_name
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=1000)
    product_price = models.FloatField()
    product_image = models.CharField(max_length=500, default="https://static.vecteezy.com/system/resources/previews/004/629/642/original/empty-shopping-bag-free-vector.jpg")


class Trainer(models.Model):
    def __str__(self):
        return self.trainer_name
    trainer_name = models.CharField(max_length=200)
    trainer_description = models.CharField(max_length=5000)
    trainer_image = models.CharField(max_length=500, default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png")

class Contact(models.Model):
    def __str__(self):
        return self.contact_name
    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    contact_message = models.CharField(max_length=800)