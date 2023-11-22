from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from vehicles.models import *
from techservice.models import *
from vehicles.forms import *
from vehicles.serializers import VehicleSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import generics

# Главная
class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            user = self.request.user
            try:
                profile = UserProfile.objects.get(user=user)
                print(f"User groups: {user.groups.all()}")
                print(f"User profile: {profile}")

                if profile.is_service:
                    print("User is a service organization.")
                    return redirect('vehicle_list')
                else:
                    print("User is a client.")
                    return redirect('vehicle_search_list')

            except UserProfile.DoesNotExist:
                print("UserProfile not found for the user.")
                return redirect('vehicle_search_list')
        else:
            return redirect('vehicle_search_list')

class VehicleSearchView(ListView):
    model = Vehicle
    template_name = 'vehicles/vehicle_search.html'
    queryset = Vehicle.objects.all()

class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicles/vehicle_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        try:
            profile = UserProfile.objects.get(user=user)
            context['user_profile'] = profile
        except UserProfile.DoesNotExist:
            pass  # Действие, если профиль не найден
        return context

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = self.request.user
            try:
                profile = UserProfile.objects.get(user=user)
                if profile.is_service:
                    return Vehicle.objects.filter(service_company=profile.service_company)
            except UserProfile.DoesNotExist:
                return Vehicle.objects.filter(client=user)
        else:
            return Vehicle.objects.all()



class VehicleDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'vehicles.view_vehicle'
    model = Vehicle
    template_name = 'vehicles/vehicle_view.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class VehicleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'vehicles.add_vehicle'
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicles/vehicle_create.html'
    success_url = reverse_lazy('vehicle_list')

class VehicleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'vehicles.change_vehicle'
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicles/vehicle_update.html'
    success_url = reverse_lazy('vehicle_list')

class VehicleDescriptionView(TemplateView):
    template_name= 'techservice/description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicle = Vehicle.objects.get(pk = self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'technic':
            context['atribute'] = vehicle.technic
            context['description'] = vehicle.technic.description 
        elif atribute == 'engine':
            context['atribute'] = vehicle.engine
            context['description'] = vehicle.engine.description 
        elif atribute == 'transmission':
            context['atribute'] = vehicle.transmission
            context['description'] = vehicle.transmission.description
        elif atribute == 'driving_bridge':
            context['atribute'] = vehicle.driving_bridge
            context['description'] = vehicle.driving_bridge.description 
        elif atribute == 'controlled_bridge':
            context['atribute'] = vehicle.controlled_bridge
            context['description'] = vehicle.controlled_bridge.description 
        elif atribute == 'equipment':
            context['atribute'] = 'Комплектация'
            context['description'] = vehicle.equipment
        elif atribute == 'service_company':
            context['atribute'] = vehicle.service_company
            context['description'] = vehicle.service_company.description
        return context

class VehicleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'vehicles.delete_vehicle'
    model = Vehicle
    template_name_suffix = '_delete'
    success_url = reverse_lazy('vehicle_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'vehicle'
        return context


# API
class VehicleListAPI(generics.ListAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

class VehicleUserListAPI(generics.ListAPIView):
    serializer_class = VehicleSerializer
    
    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Vehicle.objects.filter(client = user)
        elif type(user) == str:
            queryset = Vehicle.objects.filter(client__username = user)
        return queryset

class VehicleDetailAPI(generics.RetrieveAPIView):
    serializer_class = VehicleSerializer

    def get_object(self):
        obj = Vehicle.objects.get(pk = self.kwargs['pk'])
        return obj