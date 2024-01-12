from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Teacher(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    experience = models.IntegerField(default=0)
    specialization = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pupil(AbstractUser):
    class Meta:
        ordering = ("first_name",)

    def __str__(self):
        return f"{self.username}"


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    time = models.DateTimeField()
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )
    pupils = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="lessons_as_pupil")

    class Meta:
        ordering = ("time",)


