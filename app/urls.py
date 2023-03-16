from django.urls import path

from app import views

app_name = "app"

urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    # path('register/submit', views.submit, name='submit'),
    # path('login/verify', views.verify, name='verify'),
    path('', views.index, name='index'),
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    # path('restricted/', views.restricted, name='restricted'),
    # path('logout/', views.user_logout, name='logout'),
]
