from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='book'),
    path('book_details/', views.book_details, name='book_details'),

]
