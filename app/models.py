from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.IntegerField(primary_key=True, null=False)
    password = models.CharField(max_length=128, null=False)
    username = models.CharField(max_length=128, null=False)
    userlevel = models.IntegerField(null=False) #userlevel: 0 is normal user, 1 is admin
    def __str__(self):
        return self.username
    class Meta:
        db_table = 'User' #ensure the table in database named User, not app_user

class Book(models.Model):
    bookid = models.IntegerField(primary_key=True, null=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    booknum = models.IntegerField(null=False) #remain number
    description = models.TextField()

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'Book'


#the borrowing history
class Record(models.Model):
    rentno = models.IntegerField(primary_key=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'Record'
