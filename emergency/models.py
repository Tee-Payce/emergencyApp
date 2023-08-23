from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Add other fields as per your requirements

    def __str__(self):
        return self.name

class EmergencyContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    service = models.CharField(max_lengrh=100)
    # Add other fields as per your requirements

    def __str__(self):
        return self.name
