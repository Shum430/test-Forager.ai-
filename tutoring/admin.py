from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tutoring.models import Teacher, Pupil, Lesson


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "specialization",]
    list_filter = ["experience",]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    # list_display = ["name", "time", "teacher",]
    # add_fieldsets = m,o.add_fieldsets + (
    #     ("Additional info", {"fields": ("teacher",)}),
    # )
    pass


@admin.register(Pupil)
class PupilAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name", "email",)}),
    )
