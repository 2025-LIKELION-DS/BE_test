from django.db import models

class Professor(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Lecture(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=20, unique=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='lecture')

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20, unique=True)
#   lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='student')
    lectures = models.ManyToManyField(Lecture, through="LectureStudent", related_name='student')

    def __str__(self):
        return self.name

class LectureStudent(models.Model):
    lecture = models.ForeignKey(to=Lecture, on_delete=models.CASCADE, related_name='lecture_students')
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, related_name='lecture_students')
    enrolled_at = models.DateTimeField(auto_now_add=True)