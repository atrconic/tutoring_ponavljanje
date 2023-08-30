from django.contrib.auth.models import User
from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Mentor(User):
    pass


class Student(User):
    pass


class Course(TimeStampMixin):
    mentor_id = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=300, null=False)
    class_quantity = models.PositiveIntegerField()

    objects = models.Manager()


class Subject(TimeStampMixin):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    mentor_id = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=300, null=False)

    objects = models.Manager()


class Klass(TimeStampMixin):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mentor_id = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    started_at = models.DateTimeField(null=True)
    ended_at = models.DateTimeField(null=True)

    objects = models.Manager()




