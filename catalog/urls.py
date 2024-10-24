from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ContactsTemplateView, ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", cache_page(60)(ContactsTemplateView.as_view()), name="contacts"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("catalog/create", ProductCreateView.as_view(), name="product_create"),
    path("catalog/<int:pk>/delete", ProductUpdateView.as_view(), name="product_update"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete")
]
