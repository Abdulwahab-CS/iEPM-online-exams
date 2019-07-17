from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_examiner = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        super(MyUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
