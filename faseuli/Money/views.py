from .models import *
from django.shortcuts import get_object_or_404, render, redirect


def money_main(request):
    user=request.user
    Money_objects=Money.objects.filter(user=user)
    return render(request, 'money_main.html', {'data':Money_objects})

def money_record(req):
    new_money=Money()
    new_money.user=req.user
    new_money.cost=req.POST['cost']
    new_money.save()
    return redirect('money:main')


