from django.shortcuts import render

def index(request):
    name = "Abdur Rawf"  # You can change this value or fetch dynamically
    return render(request, 'index.html', {'name': name})
