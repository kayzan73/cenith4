from django.urls import path
from .views import DashboardView, \
    OrganizationListView, \
    OrganizationDetailView, OrganizationalUnitListView, OrganizationalUnitDetailView


app_name = 'organizations'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('organization/', OrganizationListView.as_view(), name='organization_list'),
    path('orgsnization/<int:pk>', OrganizationDetailView.as_view(), name='organization_detail'),
    path('organizational_unit/', OrganizationalUnitListView.as_view(), name='organizational_unit_list'),
    path('organizational_unit/<int:pk>', OrganizationalUnitDetailView.as_view(), name='organizational_unit_detail'),
]
