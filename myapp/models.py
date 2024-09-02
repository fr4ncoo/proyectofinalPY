from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  

    def __str__(self):
        return self.name

class Editorial(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Libro(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, null=True, blank=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title
