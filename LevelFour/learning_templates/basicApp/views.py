from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={
    'text':'Hello Work',
    'number':9001
    }
    return render(request,'basicApp/index.html',context=context_dict)

def other(request):
    return render(request,'basicApp/other.html')

def relUrl(request):
    return render(request,'basicApp/relativeURL.html')
