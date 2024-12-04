from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Student(models.Model):
  Matric_Number = models.CharField(max_length=20)
  First_Name = models.CharField(max_length=50)
  Last_Name = models.CharField(max_length=50)
  Email = models.EmailField(max_length=100)
  Field_of_Study = models.CharField(max_length=50)
  CA_Score = models.PositiveIntegerField(validators=[MaxValueValidator(30)])
  Exam_Score = models.PositiveIntegerField(validators=[MaxValueValidator(70)])
  
  def __str__(self):
    return f"Student: {self.First_Name} {self.Last_Name}"
