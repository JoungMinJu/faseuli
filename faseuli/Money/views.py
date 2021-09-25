from .models import *
from django.shortcuts import get_object_or_404, render, redirect


def money_main(request):
    Money_objects=Money.objects.all()
    return render(request, 'money_main.html', {'data':Money_objects})

def money_record(req):
    if req.method=='POST':
        Money_object=get_object_or_404(Money)
        Money_object.cost+=req.POST.get('cost')
        Money_object.save()
    return render(req, 'money_record.html')
    #redirect('/money/main')
