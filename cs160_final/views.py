from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    
    #return render(request, '/home/ubuntu/workspace/cs160_final/templates/cs160_final/index.html')
    return render(request, 'cs160_final/index.html')
    
def chapterOne(request):
    return render(request, 'cs160_final/chapterOne.html')

def chapterOneRight(request):
    return render(request, 'cs160_final/chapterOneRight.html')

def chapterOneWrong(request):
    return render(request, 'cs160_final/chapterOneWrong.html')
    
def chapterTwo(request):
    return render(request, 'cs160_final/chapterTwo.html')