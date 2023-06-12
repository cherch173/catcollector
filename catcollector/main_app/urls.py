from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # VID 1 (Intro) 
    # Part 10 Step 3) Define the Route
    path('cats/', views.cats_index, name='index'),
    # VID 2 (Models) 
    # Step 10.1 Determine the proper route for Details Page
    # (/cats/:id)
    # Step 10.3 DEFINE the DETAILS (Show functionality) ROUTE
    path('/cats/<int:cat_id>/', views.cats_details, name='detail'),
]
