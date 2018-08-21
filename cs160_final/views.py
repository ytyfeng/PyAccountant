from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    
    #return render(request, '/home/ubuntu/workspace/cs160_final/templates/cs160_final/index.html')
    return render(request, 'cs160_final/index.html')
    
def chapterZero(request):
    return render(request, 'cs160_final/chapterZero.html')
    
def chapterOne(request):
    return render(request, 'cs160_final/chapterOne.html')
    
def chapterTwo(request):
    return render(request, 'cs160_final/chapterTwo.html')
    
def chapterThree(request):
    return render(request, 'cs160_final/chapterThree.html')

def chapterFour(request):
    return render(request, 'cs160_final/chapterFour.html')

def chapterFive(request):
    return render(request, 'cs160_final/chapterFive.html')
    
def congrats(request):
    return render(request, 'cs160_final/congrats.html')

