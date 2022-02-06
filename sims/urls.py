from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('list/', views.sim_list),
    path('<int:id>/', views.detail)
]