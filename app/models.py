from django.db import models


# Create your models here.
class Book(models.Model):
    bookid = models.IntegerField(primary_key=True, null=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    booknum = models.IntegerField(null=False)  # remain number
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Book'
