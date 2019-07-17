from django.db import models
from django.utils.text import slugify
from users.models import MyUser
from django.utils import timezone


class Exam(models.Model):
    examiner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='exams')
    exam_name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    category = models.CharField(max_length=255)
    exam_creation_date = models.DateTimeField(default=timezone.datetime.now())
    is_published = models.BooleanField(default=False)
    students = models.ManyToManyField(MyUser, related_name='+')
    num_of_questions = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.exam_name)
        super(Exam, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    body = models.TextField(max_length=4096)
    op1 = models.CharField(max_length=255)
    op2 = models.CharField(max_length=255)
    op3 = models.CharField(max_length=255)
    op4 = models.CharField(max_length=255)
    correct_ans = models.IntegerField()

    def __str__(self):
        return str(self.body)


# Mapping many-to-many relationship attributes

class TakenExam(models.Model):
    student = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField()
    full_mark = models.IntegerField()
    done_date = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.student.user.username + '\'s score in ' + self.exam.exam_name + ' exam'
