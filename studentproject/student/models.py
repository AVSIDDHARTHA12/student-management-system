from django.db import models

class Student(models.Model):
    roll = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.roll} - {self.name}"


class Marks(models.Model):
    # Use OneToOneField if 1 student = 1 report card,
    # or ForeignKey if a student can have multiple marks entries (e.g. semesters/terms)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    telugu = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()

    def __str__(self):
        return f"Marks: {self.student.name} ({self.student.roll})"