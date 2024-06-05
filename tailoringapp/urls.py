from django.urls import path
from . import views
from tailoringapp.views import CreateStudents, UpdateCustomerView 
# DeleteCustomerView

urlpatterns = [
    path('home', views.home, name="home"),
    path('add_customer/', CreateStudents.as_view(), name="add_customer"),
    path('update_customer/edit/<int:pk>', UpdateCustomerView.as_view(), name="update_customer"),
    # path('delete_customer/<int:pk>/remove', DeleteCustomerView.as_view(), name="delete_customer"),
    path('delete_customer/<int:pk>', views.deletecustomers, name="delete_customer"),
    path('search/<str:name>', views.search_customers, name="search_name"),
    path('search', views.search_customers, name="search_name"),
    # path('show_customer/', HomeView.as_view(), name="show_customer"),

]