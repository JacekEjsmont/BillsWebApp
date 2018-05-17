from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from Bill.forms import UserForm
from django.views.generic import View




from rest_framework.response import Response

from .models import Bill
from .serializers import BillSerializer
# Create your views here.
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics



""" Optional class for IndexView
    Contains serialized data"""
class BillList(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "bill/index.html"
    def get(self, request):
        query = self.request.GET.get("q")
        bills = Bill.objects.all()
        #category = Category.objects.all()
        if query:
            bills = Bill.objects.order_by(query).distinct()
        serializer = BillSerializer(bills, many=True)
        return Response({"bills" :serializer.data})
    
    
class IndexView(generic.ListView):
    model = Bill
    template_name = "bill/index.html"
    context_object_name = "bills"
    
    
    
    def get_queryset(self):
        queryset = Bill.objects.filter(Customer=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.order_by(query).distinct()
        
        return queryset
        
        
#deletes Bill
class BillDelete(DeleteView):
    model = Bill
    success_url = reverse_lazy("bill:index") 
    
#Creates Bill
class BillCreate(CreateView):

    model = Bill
    fields = [ "Category", "Amount" ]
    
    def form_valid(self, form):
        #bill = form.save(commit=False)
        form.instance.Customer = self.request.user
        return super().form_valid(form)
    
    success_url = reverse_lazy("bill:index")
    


class BillEdit(UpdateView):
    model = Bill
    fields = [ "Category", "Amount", ]
    success_url = reverse_lazy("bill:index")    
    
#creates new user    
class UserFormView(View):
    form_class = UserForm
    template_name = "bill/registration_form.html"
    #blank
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form":form})
    #process from data
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            
            user = form.save(commit=False)
            #normalized data
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                if user.is_active:                    
                    login(request, user)
                    return redirect('bill:index')
                
        return render(request, self.template_name, {"form":form})
