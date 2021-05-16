from django.db import models
from django.db import models
from django.db import models
from datetime import datetime, timedelta
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

def compute_default_to():
    return datetime.now() + timedelta(days=30)

class CouponsMod(models.Model):
    name = models.CharField(max_length=10)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    valid_from = models.DateTimeField(default=datetime.now, blank=True)
    valid_to = models.DateTimeField(default=compute_default_to)
    discount = models.IntegerField(default=15, validators=[MinValueValidator(0),MaxValueValidator(100)])
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



