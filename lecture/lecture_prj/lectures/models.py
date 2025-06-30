from django.db import models
#     속성
class Professor(models.Model): #pk>-d
    # 개체
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)

class Lecture(models.Model):
    title=models.CharField(max_length=50)
    code=models.CharField(max_length=20, unique=True)
#                   외래키
    professor=models.ForeignKey(to=Professor, on_delete=models.CASCADE, related_name="professor")
    #foreignkey?
    def __str__(self):
        return self.title
        # 여기서도 ForeignKey>ManyToManyField 가능

class Student(models.Model):
    name=models.CharField(max_length=20)
    Student_id=models.CharField(max_length=20, unique=True)
    # 다대일
    # lecture=models.ForeignKey(to=Lecture, on_delete=models.CASCADE, related_name="lecture")
    lecture=models.ManyToManyField(to=Lecture, through="LectureStudent", related_name="student")
#                   관계/매핑 카디널리티
    def __str__(self):
        return self.name

class LectureStudent(models.Model):
    lecture=models.ForeignKey(to=Lecture, on_delete=models.CASCADE, related_name="lecture_student")
    student=models.ForeignKey(to=Student, on_delete=models.CASCADE, related_name="lecture_student")
    enrolled_at=models.DateTimeField(auto_now=True)


