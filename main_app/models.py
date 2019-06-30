from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_examiner = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Exam(models.Model):
    examiner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='exams')
    exam_name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    category = models.CharField(max_length=255)
    exam_creation_date = models.DateTimeField(default=timezone.datetime.now())
    published = models.BooleanField(default=False)
    students = models.ManyToManyField(MyUser, related_name='+')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.exam_name)
        super(Exam, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    body = models.CharField(max_length=4096)
    ch1 = models.CharField(max_length=255)
    ch2 = models.CharField(max_length=255)
    ch3 = models.CharField(max_length=255)
    ch4 = models.CharField(max_length=255)
    correct_ans = models.IntegerField()

    def __str__(self):
        return str(self.body)


# Mapping many-to-many relationship attributes

class TakenExam(models.Model):
    student = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField()
    done_date = models.DateTimeField(default=timezone.datetime.now())


