from django.urls import path

from mysite.resttest.views import CoursesViews, CourseViews, ClassesViews, ClassViews, MentorViews, StudentViews

urlpatterns = [
    path('courses/', CoursesViews.as_view()),
    path('courses/<int:id>/', CourseViews.as_view()),
    path('classes/', ClassesViews.as_view()),
    path('classes/<int:id>/', ClassViews.as_view()),
    path('mentors/', MentorViews.as_view()),
    path('mentors/<int:pk>/', MentorViews.as_view()),
    path('students/', StudentViews.as_view()),
]