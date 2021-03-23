from django.db import models

# Create your models here.
# Create / Insert / Add -GET
# Retrieve / Fetch - GET
# Update / Edit - PUT 
# Delete / Remmove - DELETE
class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)