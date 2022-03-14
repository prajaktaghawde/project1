from django.forms import ModelForm
from .models import student,teacher
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User






class StudentForms(ModelForm):
    class Meta:
        model=student
        fields='__all__'


class TeacherForms(ModelForm):
    class Meta:
        model =teacher
        fields = '__all__'


class RegistrationForms(UserCreationForm):
    class Meta:
        model=User
        fields={'username','email','password1','password2'}






