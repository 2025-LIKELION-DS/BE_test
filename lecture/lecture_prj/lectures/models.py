from django.db import models

# Create your models here.
class Professor(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
class Lecture(models.Model):
    title=models.CharField(max_length=50)
    code=models.CharField(max_length=20,unique=True)
    professor=models.ForeignKey(to=Professor,on_delete=models.CASCADE,related_name="lectures")

    def __str__(self):
        return f'{self.title}'
    
class Student(models.Model):
    name=models.CharField(max_length=20)
    student_id=models.CharField(max_length=20,unique=True)
    lecture=models.ManyToManyField(to=Lecture,through="LectureStudent",related_name="students")
    

    def __str__(self):
        return f'{self.name}'
    
class LectureStudent(models.Model):
    student=models.ForeignKey(to=Student,on_delete=models.CASCADE,related_name="students_lecture")
    lecture=models.ForeignKey(to=Lecture,on_delete=models.CASCADE, related_name="students_lecture") # 추가했기에 LectuerStudent 중간 테이블 생성
    enrolled_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.lecture}'