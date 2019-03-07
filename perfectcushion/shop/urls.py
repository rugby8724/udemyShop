from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('', views.allProdCat, name='allprodcat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
]
