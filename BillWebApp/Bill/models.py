from django.db import models
from datetime import datetime
from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.
#
#class Category(models.Model):
#    Category_text = models.CharField(max_length = 30)    
#    
#    def __str__(self):
#        return self.Category_text

#class UserProfile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    
#    def __str__(self):
#        return self.user.username


class Bill(models.Model):
    
    c = (("Home", "Home"), ("Finances", "Finances"), ("Daily expenses", "Daily expenses"), ("Health", "Health"),\
         ("Holidays", "Holidays"), ("Investments", "Investments"), ("Other", "Other"))
    #Customer = models.CharField(max_length = 100)
    Date = models.DateTimeField(datetime.now(), auto_now = True)
    #Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Category = models.CharField(max_length = 100, choices = c, default = "Home" )
    Amount = models.DecimalField(max_digits=10, decimal_places=2) #models.FloatField(max_length = 10) #default = 0)
    Customer = models.ForeignKey(User, unique=False, default = 0)

    def __str__(self):
        return self.Customer.username


