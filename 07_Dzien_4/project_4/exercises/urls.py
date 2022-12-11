from django.urls import path

from exercises import views


urlpatterns = [
    # Zad 1
    path('set-cookie/', views.set_cookie),
    path('show-cookie/', views.show_cookie),
    path('delete-cookie/', views.delete_cookie),

    # Zad 2
    path('add-to-cookie/', views.add_to_cookie)

]