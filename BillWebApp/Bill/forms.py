# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:44:12 2018

@author: Jack
"""
from .models import Bill

from django import forms

from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", 'email', 'password']

#