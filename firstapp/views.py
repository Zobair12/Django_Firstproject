from django.shortcuts import render

# Create your views here.
def index(request):

   name = "MD ZOBAIR AHMED"

   return render(request, 'index.html', {'name': name})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.methos == 'POST':
        
        form = ContactForm(request.POST)
    
    return render(request, 'contact.html')