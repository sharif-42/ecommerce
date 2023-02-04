from django.urls import path

from store.views.store_views import HomeView, ProductDetailsView

app_name = 'store'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<pk>', ProductDetailsView.as_view(), name='product-details'),
]
