from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.students_list, name='students_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('courses/', views.courses_list, name='courses_list'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('forgot/', views.forgot_password, name='forgot_password'),
    path('logout/', views.logout_view, name='logout'),
    # Simple admin alternative
    path('simple-admin/', views.simple_admin, name='simple_admin'),
]
