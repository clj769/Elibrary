from django.db.models import Q
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from app.models import User, Book, Record, Category, Page


# Create your views here.
class IndexView(View):
    def get(self, request):
        category_list = Category.objects.order_by('-likes')[:4]
        page_list = Page.objects.order_by('-views')[:3]

        context_dict = {}
        context_dict['categories'] = category_list
        context_dict['pages'] = page_list

        return render(request, 'index.html', context=context_dict)


def borrow_history(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')  # the tag's 'name' in html
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
        # print(data)
        return render(request, 'borrow_history.html', context=data)


def search(request):
    # the html file's tag name
    if request.method == 'POST':
        query = request.POST.get('search')
        # print(query)
        if query:
            # search in the db with title or author
            books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
            # print(books)
        else:
            # print('no book')
            books = Book.objects.none()  # empty QuerySet

    return render(request, 'search.html', {'books': books, 'query': query})


def contact_us(request):
    return render(request, 'contactus.html')


class ShowCategoryView(View):
    def create_context_dict(self, category_name_slug):
        """
        A helper method that was created to demonstarte the power of class-based views.
        You can reuse this method in the get() and post() methods!
        """
        context_dict = {}

        try:
            category = Category.objects.get(slug=category_name_slug)
            pages = Page.objects.filter(category=category).order_by('-views')

            context_dict['pages'] = pages
            context_dict['category'] = category
        except Category.DoesNotExist:
            context_dict['pages'] = None
            context_dict['category'] = None

        return context_dict

    def get(self, request, category_name_slug):
        context_dict = self.create_context_dict(category_name_slug)
        return render(request, 'category.html', context_dict)

    # @method_decorator(login_required)
    # def post(self, request, category_name_slug):
    #     context_dict = self.create_context_dict(category_name_slug)
    #     query = request.POST['query'].strip()
    #
    #     if query:
    #         context_dict['result_list'] = run_query(query)
    #         context_dict['query'] = query
    #
    #     return render(request, 'category.html', context_dict)


class GotoView(View):
    def get(self, request):
        page_id = request.GET.get('page_id')

        try:
            selected_page = Page.objects.get(id=page_id)
        except Page.DoesNotExist:
            return redirect(reverse('elib:index'))

        selected_page.views = selected_page.views + 1
        selected_page.save()

        return redirect(selected_page.url)


def book_search(request):
    # the html file's tag name
    if request.method == 'POST':
        book_query = request.POST.get('search')
        # print(query)
        if book_query:
            # search in the db with title or author
            pages = Page.objects.filter(Q(title__icontains=book_query))
            # print(books)
        else:
            # print('no book')
            pages = Page.objects.none()  # empty QuerySet

    return render(request, 'book_search.html', {'pages': pages, 'book_query': book_query})
