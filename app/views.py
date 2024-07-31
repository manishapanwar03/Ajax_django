from django.http import JsonResponse
from django.shortcuts import render
from .models import Student

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        address1 = request.POST['address1']
        print(name, age, address1)
        Student.objects.create(name=name, age=age, address=address1)
        return JsonResponse({'name': name,'age':age,'address':address1})
    
    name = Student.objects.all()
    return render(request, "index.html", context={'data': name})
