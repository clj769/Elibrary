from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Book(models.Model):
    bookid = models.IntegerField(primary_key=True, null=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    booknum = models.IntegerField(null=False)  # remain number
    description = models.TextField()
    bookpic = models.TextField(default='undefined')
    bookcategory = models.TextField(default='undefined')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Book'


# the borrowing history
class Record(models.Model):
    rentno = models.IntegerField(primary_key=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    rent_deadline = models.DateTimeField(null=True, blank=True)
    rent_sts = models.BooleanField(default=True)

    class Meta:
        db_table = 'Record'

