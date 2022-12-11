from django.urls import path

from exercises import views


urlpatterns = [
    path('set-cookie/', views.set_cookie),
    path('show-cookie/', views.show_cookie),
    path('delete-cookie/', views.delete_cookie),
]