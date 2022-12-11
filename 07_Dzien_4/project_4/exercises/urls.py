from django.urls import path

from exercises import views


urlpatterns = [
    # Zad 1
    path('set-cookie/', views.set_cookie),
    path('show-cookie/', views.show_cookie),
    path('delete-cookie/', views.delete_cookie),

    # Zad 2
    path('add-to-cookie/', views.add_to_cookie),

    # Sesja - Zad 1
    path('set-session/', views.set_session),
    path('show-session/', views.show_session),
    path('delete-session/', views.delete_session),

    # Sesja - zad 2
    path('login/', views.login_view),

    # Sesja - zad 3
    path('add-to-session/', views.add_to_session),
    path('show-all-session/', views.show_all_session),

    # Widoki klasowe
    path('hello/', views.hello),
    path('hello2/', views.HelloView.as_view()),

    # Widoki klasowe - zad 1
    path('hi/', views.hi),
    path('hi2/', views.HiView.as_view()),
]