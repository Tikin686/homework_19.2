from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Blog
from django.views.generic import ListView, DetailView, TemplateView


class ProductListView(ListView):
    model = Product
# Create your views here.

class ProductDetailView(DetailView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class BlogListView(ListView):
    model = Blog

