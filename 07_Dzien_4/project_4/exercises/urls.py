from django.urls import path

from exercises import views


urlpatterns = [
    path('set-cookie/', views.set_cookie),
]