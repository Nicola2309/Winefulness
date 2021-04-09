from django.shortcuts import render

# Create your views here.


def index(request):
    """ This function returns the index page """

    return render(request, 'home/index.html')
