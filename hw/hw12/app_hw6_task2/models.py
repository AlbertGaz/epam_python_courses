from django.db import models


class Human(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Student(Human):
    pass


class Teacher(Human):
    pass


class Homework(models.Model):
    hw_text = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created = models.DateTimeField()
    deadline = models.DurationField()


class HomeworkResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    hw = models.ForeignKey(Homework, on_delete=models.CASCADE)
    created = models.DateTimeField()
    solution = models.TextField()
