from django.db.models import Q
from django.shortcuts import render
from app.models import User,Book,Record
# Create your views here.
def borrow_history(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id') #the tag's 'name' in html
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
        return render(request, 'borrow_history.html', context=data)

def search(request):
    #the html file's tag name
    if request.method == 'POST':
        query = request.POST.get('search')
        #print(query)
        if query:
            #search in the db with title or author
            books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
            #print(books)
        else:
            #print('no book')
            books = Book.objects.none()  # empty QuerySet

    return render(request, 'search.html', {'books': books, 'query': query})



def contact_us(request):
    return render(request, 'contactus.html')