from django.db import models

# Create your models here.

class Owner(models.Model):
    o_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    contact = models.IntegerField(unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Porson(models.Model):
    porson_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    cotegory = models.ForeignKey(Category,on_delete=models.CASCADE)
    email_id = models.EmailField()
    image = models.ImageField(upload_to='photo')
    address = models.CharField(max_length=200)
    wage = models.IntegerField()
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name


