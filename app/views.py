from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.models import Book

# Create your views here.


# def book_view(request):
#     if request.method == 'GET':
#         book_title = request.GET.get('book_title')
#         if book_title:
#             books = Book.objects.filter(title=book_title)
#             data = {
#                 'books': [
#                     {
#                         'book_id': book.bookid,
#                         'book_title': book.title,
#                         'book_author': book.author,
#                         'book_num': book.booknum,
#                         'book_description': book.description,
#                     } for book in books
#                 ]
#             }
#         else:
#             data = {'books': []}
#
#
#
#     # render返回html，按app注册顺序，从templates目录下寻找
#     # 如果settings的TEMPLAES中有'DIRS': [os.path.join(BASE_DIR, 'templates')]，则从根目录开始寻找
#     return render(request, 'book_details.html',  context=data)

# def book_search(request):
#     if request.method == 'POST':
#         book_title = request.POST.get('book_title')
#         if book_title:
#             book = Book.objects.filter(title__icontains=book_title)
#             data = {
#                 'books': [
#                     {
#                         'book_id': book.bookid,
#                         'book_title': book.title,
#                         'book_author': book.author,
#                         'book_num': book.booknum,
#                         'book_description': book.description,
#                     } for app in book
#                 ]
#             }
#             return render(request, 'book_details.html', context=data)
#     return render(request, 'book_details.html')
#


from django.shortcuts import render, get_object_or_404
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import BorrowBookForm


# def book_details(request):
#    book_dict = {}
#    value = request.GET.get('id')
#    if value:
#        book_dict["book_id"] = value
#
#     book = Book.objects.filter(book_dict)
#
#     return render(request, 'book_details.html', {"book": book})
#

def book_details(request):
    if request.method == 'GET':
        book_title = request.GET.get('book_title')
        if book_title:
            books = Book.objects.filter(title__icontains=book_title)
            data = {
                'books': [
                    {
                        'book_id': book.bookid,
                        'book_title': book.title,
                        'book_author': book.author,
                        'book_num': book.booknum,
                        'book_description': book.description,
                    } for book in books
                ]
            }
        else:
            data = {'books': []}

        return render(request, 'book_details.html', context=data)


def borrow_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = Book.objects.get(bookid=book_id)
        if book.booknum == 0:
            message = "This book is currently out of stock."
            return JsonResponse({'success': False, 'message': message})
        else:
            book.booknum -= 1
            book.save()
            message = "Book borrowed successfully!"
            return JsonResponse({'success': True, 'message': message})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})


def index(request):
    if request.method == 'GET':
        book_title = request.GET.get('book_title')
        if book_title:
            books = Book.objects.filter(title__contains=book_title)
            data = {
                'books': [
                    {
                        'book_id': book.bookid,
                        'book_title': book.title,
                        'book_author': book.author,
                        'book_num': book.booknum,
                        'book_description': book.description,
                    } for book in books
                ]
            }
        else:
            data = {'books': []}

        return render(request, 'index.html', context=data)
