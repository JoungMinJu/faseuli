from .models import Challenge
from django.shortcuts import render

# Create your views here.
def newChallenge(req):
    Challenge_object=Challenge()
    if req.method=='POST':
        Challenge_object.title=req.POST['title']
        Challenge_object.cost=req.POST['cost']
        Challenge_object.goal=req.POST['goal']
        Challenge_object.now=req.POST['now']
        Challenge_object.save()
        return redirect('/challenge/main')
    return render(req,'.html', {'data': Challenge_object})

def challenge_main(request):
    return render(request, 'challenge_main.html')

def challenge_detail(request):
    return render(request, 'challenge_detail.html')

def challenge_write(request):
    return render(request, 'challenge_write.html')
