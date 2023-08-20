from django.shortcuts import redirect,render
from  .models import *
from .models import employees
from .urls import *




def index(request):
    emp=employees.objects.all()
    
    context={
        'emp':emp,
    }
    
    
    
    
    return render(request,'index.html',context)




def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        emp = employees(
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('home') 
        
    return render(request, 'index.html')  


def edit(request):
    emp = employees.objects.all()
    print(emp.id)
    context ={
        'emp': emp,
    }
    
    return redirect(request, 'index.html', context)



def update(request,id):
     if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        emp = employees(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('home') 
    
    
     return redirect(request,'index.html')
 
def delete(request,id):
    
    emp=employees.objects.filter(id=id)
    emp.delete()
    
    context ={
        'emp': emp,
    }
    return redirect('home')
    
    
    
    
    
    
    return redirect(request,'index.html',context)
     
     



    



