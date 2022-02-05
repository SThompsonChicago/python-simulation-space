from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.sim_list),
    path('list/<int:id>/', views.sim_page)
]