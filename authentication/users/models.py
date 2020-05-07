from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=250)
    emailaddress = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"( {self.username}, {self.emailaddress}, {self.password})"
