from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView

from tutoring.models import Lesson, Pupil, Teacher
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from utils.email_utils import validate_email_with_hunter
from .forms import PupilLoginForm, PupilRegistrationForm


def index(request: HttpRequest) -> HttpResponse:
    lessons = Lesson.objects.all()
    pupils = Pupil.objects.all()
    teachers = Teacher.objects.all()
    context = {
        "lessons": lessons,
        "pupils": pupils,
        "teachers": teachers
    }
    return render(request, "tutoring/index.html", context=context)


class LessonListView(generic.ListView):
    model = Lesson
    template_name = "tutoring/lesson_list.html"
    context_object_name = "lesson_list"


class LessonDetailView(generic.DetailView):
    model = Lesson


class PupilLoginView(LoginView):
    template_name = "tutoring/pupil_login.html"
    authentication_form = PupilLoginForm
    success_url = reverse_lazy("tutoring:index")


class PupilLogoutView(LogoutView):
    next_page = reverse_lazy("tutoring:index")


class PupilRegistrationView(CreateView):
    model = Pupil
    form_class = PupilRegistrationForm
    template_name = "tutoring/pupil_registration.html"
    success_url = reverse_lazy("tutoring:pupil-login")


def registration_view(request):
    if request.method == 'POST':
        form = PupilRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Use the email validation utility function
            if validate_email_with_hunter(email):
                # Email is valid, proceed with the registration
                form.save()
                # Redirect to success page or login page
                return reverse_lazy("tutoring:index")
            else:
                # Email is not valid, show an error message
                form.add_error('email', 'Invalid email address. Please try again.')

    else:
        form = PupilRegistrationForm()

    return render(request, 'tutoring/pupil_registration.html', {'form': form})
