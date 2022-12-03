from django.urls import path

from hello import views


urlpatterns = [
    path('', views.hello),
    path('2/', views.hello2),
    path('hi/', views.hi),
    path('adam/', views.adam),
    path('ewa/', views.ewa),
    path('template/<str:name>/', views.hi_name),
    path('<str:name>/', views.hello_name),
]