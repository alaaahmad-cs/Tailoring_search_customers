from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customers
from .forms import CustomersAddedForms, EditCustomersForm, DeleteCustomersForm
from django.contrib import messages 
from django.urls import reverse_lazy, reverse
# query of database contines the query
from django.db.models import Q
# Create your views here.


def home(request):
    customers = Customers.objects.all()
    return render(request, "home.html", {"customers":customers})


class CreateStudents(CreateView):

    template_name="customers.html"
    form_class = CustomersAddedForms
    success_url = reverse_lazy('home')



class UpdateCustomerView(UpdateView):
        model = Customers
        form_class = EditCustomersForm
        template_name = "update_customer.html"


    
# class DeleteCustomerView(DeleteView):
#         model = Customers
#         form_class = DeleteCustomersForm
#         template_name = "delete_customer.html"


#         def  get_context_data(self, *args,  **kwargs):

#             customers = Customers.objects.all()
#             context = super(DeleteCustomerView, self).get_context_data(*args, **kwargs)
#             customer_id = get_object_or_404(Customers, id=self.kwargs['pk'])
#             context["customer_id"] = customer_id
#             context["customers"] = customers
#             return context
        

    

   
def deletecustomers(request, pk):
    customer = Customers.objects.filter(id = pk)
    customer.delete()
    return render(request, 'delete_customer.html',{"customer":customer})

# how search the iteams inside the db
def search_customers(request):
    if request.method =="POST":
        searched = request.POST['searched']
        # serach for all attributes
        searched = Customers.objects.filter(Q(name__icontains=searched) | Q(size__icontains=searched) | Q(phone__icontains=searched) )
        # Test if not existes the data
        if not searched:
            messages.success(request, ("That Customer Not Existes!!.. Please try Again")) 
            return render(request, "search.html", {})

        else:
            return render(request, "search.html", {"searched":searched})
    else:
         return render(request, "search.html", {})

