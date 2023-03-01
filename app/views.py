from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
from app.models import User,Book,Record
# Create your views here.
def borrow_history(request):

    if request.method == 'GET':
        #user_id = request.GET.get('user_id')
        try:
            user = User.objects.get(userid=1)
        except User.DoesNotExist:
            print("User not found.")
        records = Record.objects.filter(user=user.username)
        data = {
            'records': [
                {
                    'username': record.user,
                    'booktitle': record.book,
                    'borrowdate': record.borrow_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'returndate': record.return_date.strftime('%Y-%m-%d %H:%M:%S') if record.return_date else ''
                } for record in records
            ]
        }
    return render(request, 'borrow_history.html',context=data)