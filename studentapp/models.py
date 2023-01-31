from django.db import models

# Create your models here.
class City(models.Model):
    city=models.CharField(max_length=40)
    def __str__(self):
        return f'{self.city}'
class Course(models.Model):
    course=models.CharField(max_length=40)
    def __str__(self):
        return f'{self.course}'
class Student(models.Model):
    Student_name=models.CharField(max_length=40)
    Student_age=models.IntegerField()
    Student_ph=models.BigIntegerField()
    Student_city=models.ForeignKey(City,on_delete=models.CASCADE)
    Student_course=models.ForeignKey(Course,on_delete=models.CASCADE)
