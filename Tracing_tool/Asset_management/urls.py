
from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list_create, name='company-list'),
    path('companies/<int:pk>/', views.company_detail_update_delete, name='company-detail'),
    path('employees/', views.employee_list_create, name='employee-list'),
    path('employees/<int:pk>/', views.employee_detail_update_delete, name='employee-detail'),
    path('assets/', views.asset_list_create, name='asset-list'),
    path('assets/<int:pk>/', views.asset_detail_update_delete, name='asset-detail'),
    path('assetlogs/', views.assetlog_list_create, name='assetlog-list'),
    path('assetlogs/<int:pk>/', views.assetlog_detail_update_delete, name='assetlog-detail'),
]