from django import forms
from .models import Customers

class CustomersAddedForms(forms.ModelForm):
    
    name=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    size=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Size'}))
    phone=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}))
    class Meta:
        model = Customers
        fields = '__all__'
     
class EditCustomersForm(forms.ModelForm):
    
    name=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    size=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Size'}))
    phone=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}))
    class Meta:
        model = Customers
        fields = '__all__'
     
class DeleteCustomersForm(forms.ModelForm):

    name=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    size=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Size'}))
    phone=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}))
    class Meta:
        model = Customers
        fields = '__all__'
     