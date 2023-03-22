from datetime import timedelta, datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Min
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from app.models import Book, Record


#rewrite index page
def index(request):
    #show 3 new books by largest bookid
    new_books = Book.objects.order_by('-bookid')[:3]

    #each catagory get the first id's book
    categories = Book.objects.values('bookcategory').annotate(bookid_min=Min('bookid'))
    category_books = [Book.objects.get(bookid=category['bookid_min']) for category in categories]

    data = {
        'new_books': new_books,
        'category_books':category_books,
    }

    return render(request, 'app/index.html', context=data)

# Create your views here.
# class IndexView(View):
#     def get(self, request):
#         category_list = Category.objects.order_by('-likes')[:4]
#         page_list = Page.objects.order_by('-views')[:3]
#
#         context_dict = {}
#         context_dict['categories'] = category_list
#         context_dict['pages'] = page_list
#
#         return render(request, 'app/index.html', context=context_dict)


@login_required
def borrow_history(request):
    if request.method == 'GET':
        #user_id = request.GET.get('user_id')  # the tag's 'name' in html
        user_id = request.user.id
        print(user_id)
        records = Record.objects.filter(user=user_id)
        data = {
            'records': [
                {
                    'username': record.user.username,
                    'book_id': record.book.bookid,
                    'book_title': record.book.title,
                    'borrow_date': record.borrow_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'return_date': record.return_date.strftime('%Y-%m-%d %H:%M:%S') if record.return_date else ''
                } for record in records
            ]
        }
        #print(data)
        return render(request, 'app/borrow_history.html', context=data)


def search(request):
    # the html file's tag name
    if request.method == 'POST':
        query = request.POST.get('search')
        #print(query)
        if query:
            # search in the db with title or author
            books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
            #print(books)
        else:
            print('search no book')
            books = Book.objects.none()  # empty QuerySet

    return render(request, 'app/book_search.html', {'books': books, 'query': query})



def contact_us(request):
    return render(request, 'app/contactus.html')


# class ShowCategoryView(View):
#     def create_context_dict(self, category_name_slug):
#         """
#         A helper method that was created to demonstarte the power of class-based views.
#         You can reuse this method in the get() and post() methods!
#         """
#         context_dict = {}
#
#         try:
#             category = Category.objects.get(slug=category_name_slug)
#             pages = Page.objects.filter(category=category).order_by('-views')
#
#             context_dict['pages'] = pages
#             context_dict['category'] = category
#         except Category.DoesNotExist:
#             context_dict['pages'] = None
#             context_dict['category'] = None
#
#         return context_dict
#
#     def get(self, request, category_name_slug):
#         context_dict = self.create_context_dict(category_name_slug)
#         return render(request, 'app/category.html', context_dict)
#
#
# class GotoView(View):
#     def get(self, request):
#         page_id = request.GET.get('page_id')
#
#         try:
#             selected_page = Page.objects.get(id=page_id)
#         except Page.DoesNotExist:
#             return redirect(reverse('elib:index'))
#
#         selected_page.views = selected_page.views + 1
#         selected_page.save()
#
#         return redirect(selected_page.url)


def book_details(request, book_id):

    book =Book.objects.get(bookid=book_id)

    # find 3 related books
    related_books = Book.objects.filter(bookcategory=book.bookcategory).exclude(bookid=book_id)[:3]
    #print(book)
    data = {
        'book': book,
        'related_books': related_books,
    }
    #print(data)
    return render(request, 'app/book_details.html', context=data)


@login_required
def borrow_book(request):
    print('borrow_book')
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        print(book_id)
        book = Book.objects.get(bookid=book_id)
        print(book)

        if book.booknum == 0:
            message = "This book is currently out of stock."
            return JsonResponse({'success': False, 'message': message})
        else:
            book.booknum -= 1
            book.save()

            #add borrow_record
            rent_deadline = datetime.now() + timedelta(days=30)
            record = Record(user=request.user, book=book, rent_deadline=rent_deadline, rent_sts=False)
            record.save()

            message = "Book borrowed successfully!"
            return JsonResponse({'success': True, 'message': message})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})


@login_required
def personal_page(request):
    uid = request.user.id
    records = Record.objects.filter(user=uid)

    data = {
        'records': [
            {
                'book_pic': record.book.bookpic,
                'username': record.user.username,
                'user_id': record.user,
                'book_id': record.book.bookid,
                'book_name': record.book.title,
                'borrow_date': record.borrow_date.strftime('%Y-%m-%d %H:%M:%S'),
                'deadline': record.rent_deadline.strftime('%Y-%m-%d %H:%M:%S'),
            } for record in records
        ],
        'username': request.user.username,
        'uid': uid,
        'date_joined': request.user.date_joined,
    }

    print(data)
    return render(request, 'app/personalPage.html', context=data)


def recommends(request):
    if request.method == 'GET':
        category = request.GET.get('category')
        if category:
            books = Book.objects.filter(bookcategory=category)
            data = {
                'books': [
                    {
                        'book_pic': book.bookpic,
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

        return render(request, 'app/recommends.html', context=data)
