from .models import *
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render, redirect

def challenge_main(request):
    user=request.user
    data=Challenge.objects.filter(user=user)
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
    history_data=data.history.all().order_by('-date')
    p=(len(history_data)/int(data.goal))*100
    if p>=100:
        p=100
    total_cost=0
    for h in history_data:
        total_cost=total_cost+h.cost
    return render(request, 'challenge_detail.html', {'data':data, 'history_data':history_data,'p':p,'total_cost':total_cost})

def new_history(req,id): #??
    History_object=History()
    Challenge_object=get_object_or_404(Challenge, pk=id)
    history_cost=Challenge_object.cost
    History_object.cost=history_cost
    History_object.challenge=Challenge_object
    History_object.save()
    return redirect('challenge:detail',id)

def challenge_write(req):
    Challenge_object=Challenge()
    if req.method=='POST':
        Challenge_object.user=req.user
        Challenge_object.title=req.POST['title']
        Challenge_object.cost=req.POST['cost']
        Challenge_object.goal=req.POST['goal']
        Challenge_object.save()
        return redirect('challenge:main')
    return render(req,'challenge_write.html', {'data': Challenge_object})

def challenge_delete(req, id):
    delete_data = Challenge.objects.get(id=id)
    delete_data.delete()
    return redirect('challenge:main')