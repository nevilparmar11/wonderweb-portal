from django.db import models

class submites(models.Model):
    key = models.CharField(max_length=10,primary_key=True)
    issubmitted = models.BooleanField(default=False)

class submissions(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=10,primary_key=True)
    file = models.ImageField(upload_to="submissions")
    time = models.DateField(auto_now=True)

