from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', VehicleSearchView.as_view(), name='vehicle_search_list'),
    path('vehicles/', VehicleListView.as_view(), name='vehicle_list'),
    path('vehicle/<pk>/detail', VehicleDetailView.as_view(), name='vehicle_detail'),
    path('vehicle/create', VehicleCreateView.as_view(), name='vehicle_create'),
    path('vehicle/<pk>/update', VehicleUpdateView.as_view(), name='vehicle_update'),
    path('vehicle/<pk>/delete', VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('vehicle/<pk>/description/<atribute>', VehicleDescriptionView.as_view(), name='vehicle_description'),

    path('api/vehicles/',VehicleListAPI.as_view(),name='vehicle_list_api'),
    path('api/<user>/vehicles/',VehicleUserListAPI.as_view(),name='user_vehicle_list_api'),
    path('api/vehicle/<pk>/',VehicleDetailAPI.as_view(),name='vehicle_detail_api'),
]
