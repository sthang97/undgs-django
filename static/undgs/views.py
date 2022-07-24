from django.shortcuts import render

def home(request):
    #return HttpResponse('Homepage')
    return render(request, 'home.html')
