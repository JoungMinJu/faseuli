from django.shortcuts import render

def challenge_main(request):
    return render(request, 'challenge_main.html')

def challenge_detail(request):
    return render(request, 'challenge_detail.html')

def challenge_write(request):
    return render(request, 'challenge_write.html')
