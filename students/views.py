from .models import Student
from .forms import StudentForm
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
  return render(request, "students/index.html", {
    "students": Student.objects.all()
  })

def view_student(request, id):
  student = Student.objects.get(pk=id)
  return HttpResponseRedirect(reverse("index"))

def add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
             new_matric_number = form.cleaned_data["Matric_Number"]
             new_first_name = form.cleaned_data["First_Name"]
             new_last_name = form.cleaned_data["Last_Name"]
             new_email = form.cleaned_data["Email"]
             new_gender = form.cleaned_data["Gender"]
             new_field_of_study = form.cleaned_data["Field_of_Study"]
             new_ca_score = form.cleaned_data["CA_Score"]
             new_exam_score = form.cleaned_data["Exam_Score"]

             new_student = Student(
                Matric_Number = new_matric_number,
                First_Name = new_first_name,
                Last_Name = new_last_name,
                Email = new_email,
                Gender = new_gender,
                Field_of_Study = new_field_of_study,
                CA_Score = new_ca_score,
                Exam_Score = new_exam_score
             )
             new_student.save()
             return render(request, "students/add.html", {
                "form": StudentForm(),
                "success": True
             })
    else:
        form = StudentForm()
    return render(request, "students/add.html", {
        "form": StudentForm()
    })

def edit(request, id):
    if request.method == "POST":
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, "students/edit.html", {
                "form": form,
                "success": True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, "students/edit.html", {
        "form": form
    })

def delete(request, id):
    if request.method == "POST":
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse("index"))