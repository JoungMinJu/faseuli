from django.shortcuts import render

def main(request):
    return render(request, 'money_main.html')

def record(request):
    return render(request, 'money_record.html')
