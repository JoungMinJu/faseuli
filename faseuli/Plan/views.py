from django.shortcuts import render

def plan_main(request):
    return render(request, 'plan_main.html')

def plan_add(request):
    return render(request, 'plan_add.html')
