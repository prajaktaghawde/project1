from django.shortcuts import render,redirect
from  .forms import StudentForms,TeacherForms,RegistrationForms
from  django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def student(request):
    form=StudentForms
    if request.method=='POST':
        stud_form=StudentForms(request.POST)


        if stud_form.is_valid():
            stud_form.save()
            return redirect('/student')
    return render(request,'student.html',{'form':form})

def teacher(request):
    form=TeacherForms
    if request.method=='POST':
       teacher_form = TeacherForms(request.POST)
       if teacher_form.is_valid():
           teacher_form.save()
           return redirect('/teacher')
    return render(request,'teacher.html',{'form':form})


def register(request):
    form=RegistrationForms
    if request.method=='POST':
       register_form = RegistrationForms(request.POST)
       if register_form.is_valid():
           register_form.save()
           return redirect('/register')
    return render(request,'register.html',{'form':form})











