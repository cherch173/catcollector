from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Part 10 Step 3) Define the Route
    path('cats/', views.cats_index, name='index'),
]
