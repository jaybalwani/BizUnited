from django.shortcuts import render

# Create your views here.

def getConsultants(request):
    return render(request, 'consultants/posts.html')
