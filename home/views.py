from django.shortcuts import render
from .form import BookForms
from .models import Book

# Create your views here.

def form_view(request):
    if request.method == 'POST'
    form = BookForms(request.POST)
    if form
    form = CustomForms()
   # book= Book.objects.all()
   # book= Book.objects.filter(name='', purchase_date='')

    context = {
        "head":"Custom form created here using python",
        "forms":form
    }
     
    return render(request,'forms.html',context)
    return render(request,'h1.html')

#def design(request):
   # return render(request,'design.html')