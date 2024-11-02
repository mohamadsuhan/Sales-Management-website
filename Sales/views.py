from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Sales.models import Student

user1 = None


# Create your views here.
def login_fun(request):
    global user1
    if request.method == 'POST':
        name=request.POST['txtname']
        password = request.POST['txtpw']
        global user
        user=authenticate(username=name,password=password)
        if user is not None:
            if user.is_superuser:
                user1 = 'admin'
                return render(request,'home.html')
            elif user.is_authenticated:
                return HttpResponse("welcome to sales page")
            else:
                pass
        else:
            return render(request, 'login.html')

    else:
        return render(request,'login.html')





def signup_fun(request):
    if request.method=='POST':
        name=request.POST['txtname']
        Password = request.POST['txtpw']

        if User.objects.filter((Q (username=name))).exists():
            data = {'msg':True}
            return render(request, 'signup.html',data)
        else:
            user1=User.objects.create_user(username=name,password=Password)
            user1.save()
            return redirect('log')

    else:
        return render(request,'signup.html')




def addstudent(request):
    if request.method == 'POST':
        s1 = Student()
        if user1 == 'admin':
            s1.sales_person_id = request.POST['sales_person']
        else:
            s1.sales_person=user
        s1.joiningdate = request.POST['txtdate']
        s1.name = request.POST['txtname']
        s1.age = request.POST['txtage']
        s1.mobile = request.POST['txtmobile']
        s1.email = request.POST['txtemail']
        s1.education = request.POST['education']
        s1.skills = request.POST['txtskills']
        s1.save()
        return redirect('Display')
    else:
        print(user1)
        users= User.objects.all()
        return render(request, 'add.html',{'users':users})


def DisplayStudent(request):
    if request.user.is_superuser:
        students= Student.objects.all()
        return render(request,'Display.html',{'students':students,'salesperson':True,'update':True})
    else:
        students = Student.objects.filter(sales_person=user)
        return render(request, 'Display.html', {'students': students,'salesperson':False,'update':False})


def homestudent(request):
    if user1 == 'admin':
        return render(request,'home.html')
    else:
        return render(request, 'Display.html', {'sales':True,'user':user})


def Update_student(request, id):
    users = User.objects.all()
    s1 = Student.objects.get(id=id)
    if request.method == 'POST':
        s1.sales_person_id = request.POST['sales_person']
        s1.joiningdate = request.POST['txtdate']
        s1.name = request.POST['txtname']
        s1.age = request.POST['txtage']
        s1.mobile = request.POST['txtmobile']
        s1.email = request.POST['txtemail']
        s1.education = request.POST['education']
        s1.skills = request.POST['txtskills']
        s1.save()
        return redirect('Display')
    else:
        return render(request,'add.html',{'users':users,'students':s1})
    return HttpResponse('update')


def Delete_student(request,id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect('Display')