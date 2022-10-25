from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WishList(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    item=models.CharField(max_length=500,null=True, blank=True)
    price=models.CharField(max_length=500,null=True, blank=True)
    seller=models.CharField(max_length=500,null=True, blank=True)
    image=models.URLField(max_length=500,null=True, blank=True)
    link=models.URLField(max_length=500,null=True, blank=True)

    def __str__(self):
        return self.item
