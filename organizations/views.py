from django.views.generic import TemplateView, ListView, DetailView
from . import models

class DashboardView(TemplateView):
    template_name = "organizations/dashboard.html"


class OrganizationDetailView(DetailView):
    template_name = "organizations/organization_details.html"
    model = models.Organization


class OrganizationListView(ListView):
    template_name = "organizations/organization_list.html"
    model = models.Organization


class OrganizationalUnitDetailView(DetailView):
    template_name = "organizations/organizational_unit_details.html"
    model = models.OrganizationalUnit


class OrganizationalUnitListView(ListView):
    template_name = "organizations/organizational_unit_list.html"
    model = models.OrganizationalUnit
