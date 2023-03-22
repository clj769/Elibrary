from django import forms
from app.models import Book


class BorrowBookForm(forms.Form):
    book_id = forms.IntegerField()

    def borrow_book(self):
        book_id = self.cleaned_data['book_id']
        book = Book.objects.get(pk=book_id)
        book.book_num -= 1
        book.save()

