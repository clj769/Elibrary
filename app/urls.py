from django.urls import path
from app import views

app_name = 'elib'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<slug:category_name_slug>/', views.ShowCategoryView.as_view(), name='show_category'),
    path('borrow_history/', views.borrow_history, name='borrow_history'),
    path('contactus/', views.contact_us, name='contact_us'),
    #path('search/', views.search, name='search'),
    path('book_search/', views.book_search, name='book_search'),
    path('goto/', views.GotoView.as_view(), name='goto'),

]
