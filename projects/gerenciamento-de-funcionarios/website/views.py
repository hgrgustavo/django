from django.urls import reverse_lazy
from django.views.generic import *
from helloworld.models import Employee

"""
class ListEmployee(ListView):
    template_name = "templates/funcionarios.html"
    model = Employee
    context_object_name = "employees"
"""


class IndexTemplateView(TemplateView):
    template_name = "index.html"


class EmployeeListView(ListView):
    template_name = "website/list.html"
    model = Employee
    context_object_name = "employee_list"


class EmployeeUpdateView(UpdateView):
    template_name = "update.html"
    model = Employee
    fields = "__all__"
    context_object_name = "employee"

    def get_object(self, queryset=None):
        employee = None
        e_id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if e_id is not None:
            employee = Employee.objects.filter(id=e_id).first()
        elif slug is not None:
            slug_field = self.get_slug_field()
            employee = Employee.objects.filter(**{slug_field: slug}).first()

        return employee


class EmployeeDeleteView(DeleteView):
    template_view = "website/delete.html"
    model = Employee
    context_object_name = "employee"
    success_url = reverse_lazy("website:employee_list")


class EmployeeCreateView(CreateView):
    template_name = "website/create.html",
    model = Employee
    form_class = InsertEmployeeForm
    success_url = reverse_lazy("website:employee_list")




