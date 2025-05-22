from django.db import models

class Professor(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)

class Lecture(models.Model):
    title=models.CharField(max_length=50)
    code=models.CharField(max_length=20, unique=True)
    professor=models.ForeignKey(to=Professor, on_delete=models.CASCADE, related_name="professor")
    #foreignkey?
    def __str__(self):
        return self.title

class Student(models.Model):
    name=models.CharField(max_length=20)
    Student_id=models.CharField(max_length=20, unique=True)
    lecture=models.ForeignKey(to=Lecture, on_delete=models.CASCADE, related_name="lecture")
    
    def __str__(self):
        return self.name