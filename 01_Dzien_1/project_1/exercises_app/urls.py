from django.urls import path

from exercises_app import views

urlpatterns = [
    path('hello/', views.hello),
    path('random/', views.random_view),
]