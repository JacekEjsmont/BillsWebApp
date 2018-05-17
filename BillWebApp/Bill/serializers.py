# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:03:40 2018

@author: Jack
"""

from rest_framework import serializers
from .models import Bill

class BillSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Bill
        fields = ("__all__")
        
#class CategorySerializer(serializers.ModelSerializer):
#    
#    class Meta():
#        model = Category
#        fields = ("__all__")
# "Customer", "Date", "Amount"        