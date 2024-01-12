from django.urls import path

from tutoring.views import index, LessonListView, LessonDetailView, PupilLoginView, PupilLogoutView, \
    PupilRegistrationView

urlpatterns = [
    path("", index, name="index"),
    path("lessons/", LessonListView.as_view(), name="lesson-list"),
    path("lessons/<int:pk>/", LessonDetailView.as_view(), name="lesson-detail"),
    path('login/', PupilLoginView.as_view(), name='pupil-login'),
    path('logout/', PupilLogoutView.as_view(), name='pupil-logout'),
    path('register/', PupilRegistrationView.as_view(), name='pupil-registration'),
]

app_name = "tutoring"
