from .models import *
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render, redirect

def challenge_main(request):
    data=Challenge.objects.all().order_by('-id')
    sum=Challenge.objects.aggregate(Sum('cost'))
    return render(request, 'challenge_main.html', {'data':data, 'sum':sum['cost__sum']})

#def challenge_detail(request, id):
 #   Challenge_object=get_object_or_404(Challenge, pk=id)
  #  all_history=Challenge_object.history.all()
 #   data={
  #      'challenge' : Challenge_object,
  #      'history': all_history
  #  }
  #  return render(request, 'challenge_detail.html')

def challenge_detail(request, id):
    data=get_object_or_404(Challenge, pk=id)
    history_data=History.objects.all()
  
    return render(request, 'challenge_detail.html', {'data':data, 'history_data':history_data})

def new_history(req,id): #??
    if req.method=='POST':
        Challenge_object=get_object_or_404(Challenge, pk=id)
        history_cost=req.POST.get('cost')
        history_date=req.POST.get('date')
        History.objects.create(
            cost=history_cost,
            date=history_date,
            challenge=Challenge_object
        )
    return redirect('/challenge/detail/'+str(id)+'/')

def challenge_write(req):
    Challenge_object=Challenge()
    if req.method=='POST':
        Challenge_object.title=req.POST['title']
        Challenge_object.cost=req.POST['cost']
        Challenge_object.goal=req.POST['goal']
        Challenge_object.save()
        return redirect('/challenge/main')
    return render(req,'challenge_write.html', {'data': Challenge_object})

def challenge_delete(req, id):
    delete_data = Challenge.objects.get(id=id)
    delete_data.delete()
    return redirect('/challenge/main')