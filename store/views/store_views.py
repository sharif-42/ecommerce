from django.views.generic import ListView, DetailView,  View
from django.shortcuts import render
from django.views import View

from product.models import Product


class HomeView(ListView):
    model = Product
    paginate_by = 10
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = ""
        return context


class ProductDetailsView(DetailView):
    model = Product
    template_name = "product_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context