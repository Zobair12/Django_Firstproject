from django.shortcuts import render

# Create your views here.
def index(request):

   name = "MD ZOBAIR AHMED"

   return render(request, 'index.html', {'name': name})

def about(request):
    return render(request, 'about.html')