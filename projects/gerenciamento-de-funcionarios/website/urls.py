from django.urls import path

from helloworld.models import Employee
from .views import IndexTemplateView, EmployeeListView, EmployeeUpdateView, EmployeeDeleteView, EmployeeCreateView

app_name = "website"
urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),

    path("employees/", EmployeeListView.as_view(), name="employee_list"),

    path("employees/<id>", EmployeeUpdateView.as_view(), name="employee_update"),
    path("employees/<slug>", EmployeeUpdateView.as_view(), name="employee_update"),

    path("employee/delete/<pk>", EmployeeDeleteView.as_view(), name="employee_delete"),

    path("employee/register/", EmployeeCreateView.as_view(), name="employee_register")



]
