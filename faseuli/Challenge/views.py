from .models import Challenge, History
from django.shortcuts import render

def challenge_main(request):
    data=Challenge.objects.all()
    return render(request, 'challenge_main.html', {'data':data})

def challenge_detail(request, id):
    Challenge_object=get_object_or_404(Challenge, pk=id)
    History_object=Challenge_object.History_set.all()
    data={
        'challenge' : Challenge_object,
        'history' : History_object
    }
    return render(request, 'challenge_detail.html', data)

def new_history(req,id): #??
    if req.method=='POST':
        History_object=History()
        History_object.date=req.POST['date']
        History_object.cost=req.POST['cost']
        History_object.Challenge=id
        History_object.save()
    return redirect('/challenge/detail/'+int(id))

def challenge_write(req):
    Challenge_object=Challenge()
    if req.method=='POST':
        Challenge_object.title=req.POST['title']
        Challenge_object.cost=req.POST['cost']
        Challenge_object.goal=req.POST['goal']
        Challenge_object.save()
        return redirect('/challenge/main')
    return render(req,'challenge_write.html', {'data': Challenge_object})
