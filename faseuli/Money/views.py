from django.shortcuts import render

def money_main(request):
    return render(request, 'money_main.html')

def money_record(request):
    return render(request, 'money_record.html')
