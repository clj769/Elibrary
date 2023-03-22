from django.urls import path
from app import views

app_name = 'elib'

urlpatterns = [
    path('', views.index, name='index'),

    path('borrow_history/', views.borrow_history, name='borrow_history'),
    path('contactus/', views.contact_us, name='contact_us'),
    path('search/', views.search, name='search'),

    # book details
    path('book_details/<int:book_id>/', views.book_details, name='book_details'),
    path('borrow_book/', views.borrow_book, name='borrow_book'),

    # personal page
    path('personal_page/', views.personal_page, name='personal_page'),

    # recommends
    path('recommends/', views.recommends, name='recommends'),

]
