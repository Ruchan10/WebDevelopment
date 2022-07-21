from django.shortcuts import render

# Create your views here.
# creating function to return files
def home(request):
    print(request)
    return render(request, 'home.html')