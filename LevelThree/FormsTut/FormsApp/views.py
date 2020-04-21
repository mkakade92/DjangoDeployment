from django.shortcuts import render
from FormsApp import forms

# Create your views here.
def index(request):
    return render(request,'FormsApp/index.html')

def form_name_view(request):
    form=forms.FormName()
    if request.method=="POST":
        form=forms.FormName(request.POST)

        if form.is_valid():
            #do something
            print("Success asdl;as;ldjas;ldasl;")
            print("Name ",form.cleaned_data['name'])
        else:
            print("WTF")
    return render(request,'FormsApp/forms.html',{'form':form})
