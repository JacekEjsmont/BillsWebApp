# -*- coding: utf-8 -*-
"""
Created on Mon May 14 21:42:41 2018

@author: Jack
"""

from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout



urlpatterns = [
        #bills/
url(r'^$', views.IndexView.as_view(), name="index"),
url(r'^register$', views.UserFormView.as_view(), name="register"),
url(r'^login$', login, {'template_name':'Bill/login_form.html'}, name='login'),
url(r'^logout$', logout, {'next_page':'bill:login'}, name='logout'),
url(r'^BillAdd/$', views.BillCreate.as_view(), name="bill_add"),
url(r'^(?P<pk>[0-9]+)/delete/$', views.BillDelete.as_view(), name="bill_delete" ),
url(r'^(?P<pk>[0-9]+)/edit/$', views.BillEdit.as_view(), name="bill_edit" ),
]
