from django.shortcuts import render

def main(request):
    return render(request, 'challenge_main.html')

def detail(request):
    return render(request, 'challenge_detail.html')

def write(request):
    return render(request, 'challenge_write.html')
