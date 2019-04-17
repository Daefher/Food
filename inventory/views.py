from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import articulo
from .forms import articulo_model_form
 

from django.views.generic import (
        ListView,
        CreateView,
        DetailView,
        UpdateView,
        DeleteView
)

class inventory_list(LoginRequiredMixin,ListView):
        template_name = 'inventory_list.html'
        queryset = articulo.objects.all()
        login_url = '/users/login/'

class create_product(LoginRequiredMixin,CreateView):
        template_name = 'create_product.html'
        form_class = articulo_model_form
        login_url = '/users/login/'

class update_product(LoginRequiredMixin,UpdateView):
        template_name = 'create_product.html'
        form_class = articulo_model_form
        success_message = "Registro actualizado exitosamente"
        login_url = '/users/login/'

        def get_object(self):
                id_ = self.kwargs.get("pk")
                return get_object_or_404(articulo, pk=id_)

class detail_product(LoginRequiredMixin,DetailView):
        template_name = 'detail_product.html'
        form_class = articulo_model_form     
        login_url = '/users/login/'   

        def get_object(self):
                id_ = self.kwargs.get("pk")
                return get_object_or_404(articulo, pk=id_)

class delete_product(LoginRequiredMixin,DeleteView):
        model = articulo
        success_url = reverse_lazy('inventory:list-view')
        login_url = '/users/login/'

        def get_object(self):
                id_ = self.kwargs.get("pk")
                return get_object_or_404(articulo, pk=id_)