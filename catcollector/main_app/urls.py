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
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    # VID 3 (CBVs)
    # Step 5 Part 3 DEFINE the CREATE ROUTE (new cat)
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    # Step 6 Part 1 DEFINE the UPDATE *and* DELETE ROUTES as they're similar
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),

]
