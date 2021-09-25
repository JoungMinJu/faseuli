from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def plan_main(request):
    user=request.user
    user_hobby=user.hobby 
    #user의 hobby를 가져옴
    plans=Plan.objects.filter(user=user)
    #recommend=로 해서 유저의 hobby에 따른 추천목록을 보여줘야함.
    recommend=RecommendPlan.objects.filter(hobby=user_hobby)
    return render(request,'plan_main.html',{'plans':plans,'recommend':recommend})

#플랜 작성하는 페이지로 이동하는 함수
def plan_add(request): 
    return render(request, 'plan_add.html')

def plan_create(request): 
    new_plan=Plan()
    new_plan.user=request.user
    new_plan.title=request.POST['title']
    new_plan.goal=request.POST['goal']
    new_plan.image=request.FILES.get('image')
    new_plan.save()
    #메인페이지로 이동??
    return redirect('plan:main')

def plan_del(request,id):
    delete=Plan.objects.get(id=id)
    delete.delete()
    return redirect('plan:main')

def edit_plan(request, id):
    edit=Plan.objects.get(id=id)
    #edit_plan.html로 이동
    return render(request, 'plan/plan_edit.html',{'plans':edit})

def update_plan(request,id):
    update_plan=Plan.objects.get(id=id)
    update_plan.user=request.user
    update_plan.title=request.POST['title']
    update_plan.goal=request.POST['goal']
    update_plan.image=request.FILES.get('image')
    update_plan.save()
    return redirect('plan:main')
    