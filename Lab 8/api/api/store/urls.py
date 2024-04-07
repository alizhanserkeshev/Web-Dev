from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('store/', views.store, name="store"),
    path('store/details/<int:id>', views.details, name='details')
    
]
