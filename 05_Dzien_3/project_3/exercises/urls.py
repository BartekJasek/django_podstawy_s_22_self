from django.urls import path

from exercises import views

urlpatterns = [
    path('1/', views.one),
]