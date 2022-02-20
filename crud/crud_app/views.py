from django.shortcuts import render
from crud_app import forms
from crud_app.models import Student

# Create your views here.

def index(request):

    student_list = Student.objects.order_by('first_name')
    diction = {'title': "index", 'student_list': student_list}
    
    return render(request, 'crud_app/index.html', context= diction)


def student_form(request):
    form = forms.StudentForm()

    if request.method == "POST":
        form = forms.StudentForm(request.POST)

        if form.is_valid():
            form.save(commit= True)
            return index(request)

    diction ={'title': student_form, 'student_form': form}
    return render( request, 'crud_app/student_form.html', context= diction)


def student_info(request,student_id):
    student_info = Student.objects.get(pk=student_id)
    diction = {'student_info': student_info}
    return render( request, 'crud_app/student_info.html', context= diction)

        
def student_update(request,student_id):
    student_update = Student.objects.get(pk=student_id)
   
    form = forms.StudentForm(instance=student_update)


    if request.method=='POST':
        form= forms.StudentForm(request.POST, instance=student_update)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction= {'student_form':form}        
    return render(request,'crud_app/student_update.html', context= diction)


def student_delete(request,student_id):
    student = Student.objects.get(pk=student_id).delete()
    diction = {'delete_message': "Delete Done"}
    return render( request, 'crud_app/student_delete.html', context= diction)

