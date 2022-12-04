from django.urls import path

from intro import views

urlpatterns = [
    path('home/', views.home)
]