from django.shortcuts import render, redirect
from firstapp.forms import ContactForm
from django.contrib import messages
from firstapp.models import Contact

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
    
    form = ContactForm()
    
    return render(request,'contact.html', {'form': form})


def contact_list(request):
    contacts = Contact.objects.all()
   
    return render(request, 'contact_list.html', {'contacts':contacts})