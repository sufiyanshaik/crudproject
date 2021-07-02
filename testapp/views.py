from django.shortcuts import render,redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm
from django.http import HttpResponseRedirect
# Create your views here.
def retrieve(request):
    employees=Employee.objects.all()
    return render(request,'testapp/home.html',{'employees':employees})


def create(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'testapp/create.html',{'form':form})

def delete(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return HttpResponseRedirect('/')

def update(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'testapp/update.html',{'emp':emp})
