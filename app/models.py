from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


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


class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=10)

    def __str__(self):
        return self.title
