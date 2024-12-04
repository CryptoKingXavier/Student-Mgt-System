from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            "Matric_Number": "Matric Number",
            "First_Name": "First Name",
            "Last_Name": "Last Name",
            "Email": "Email",
            "Field_of_Study": "Field of Study",
            "CA_Score": "CA Score",
            "Exam_Score": "Exam Score"
        }
        widgets = {
            "Matric_Number": forms.TextInput(attrs={"class": "form-control"}),
            "First_Name": forms.TextInput(attrs={"class": "form-control"}),
            "Last_Name": forms.TextInput(attrs={"class": "form-control"}),
            "Email": forms.EmailInput(attrs={"class": "form-control"}),
            "Field_of_Study": forms.TextInput(attrs={"class": "form-control"}),
            "CA_Score": forms.NumberInput(attrs={"class": "form-control"}),
            "Exam_Score": forms.NumberInput(attrs={"class": "form-control"})
        }