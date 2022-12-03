from django.urls import path

from exercises_app import views

urlpatterns = [
    path('hello/', views.hello),
    path('random/', views.random_view),
    path('random/<int:max_number>/', views.random_view_2),
    path('random/<int:min_number>/<int:max_number>/', views.random_view_3),

    path('hello_name/<str:name>/', views.hello_name),
]