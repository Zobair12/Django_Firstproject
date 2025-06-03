from django.shortcuts import render, redirect
from firstapp.forms import ContactForm
from django.contrib import messages

# Create your views here.
def index(request):

   name = "MD ZOBAIR AHMED"

   return render(request, 'index.html', {'name': name})

def about(request):
    return render(request, 'about.html')

def contact(request):
    print(request.POST)
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank for contacting with us.')
            return redirect('/')
        else:
            messages.error(request,'Invalid date.')
            return redirect('contact')
    
    return render(request,'contact.html')