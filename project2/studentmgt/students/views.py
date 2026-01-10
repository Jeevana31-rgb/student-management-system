from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Count
from .models import Student, Course, User
from .forms import SignUpForm, StudentForm, CourseForm
import json


def index(request):
    """Login page"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'redirect': '/dashboard/'})
        else:
            return JsonResponse({
                'success': False,
                'message': 'Incorrect username or password'
            })
    
    return render(request, 'index.html')


def signup_view(request):
    """Sign up page"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({
                'success': True,
                'message': 'Account created. You can now log in.',
                'redirect': '/'
            })
        else:
            errors = []
            for field, error_list in form.errors.items():
                for error in error_list:
                    errors.append(error)
            return JsonResponse({
                'success': False,
                'message': ' '.join(errors)
            })
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})


@login_required
def dashboard(request):
    """Dashboard page"""
    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    
    context = {
        'total_students': total_students,
        'total_courses': total_courses,
        'user': request.user
    }
    return render(request, 'dashboard.html', context)


@login_required
def students_list(request):
    """Students list page"""
    students = Student.objects.select_related('course').all()
    context = {
        'students': students
    }
    return render(request, 'students.html', context)


@login_required
def add_student(request):
    """Add student page"""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student saved successfully.')
            return redirect('students_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = StudentForm()
    
    courses = Course.objects.all()
    context = {
        'form': form,
        'courses': courses
    }
    return render(request, 'add-student.html', context)


@login_required
def edit_student(request, student_id):
    """Edit student page"""
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('students_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = StudentForm(instance=student)
    
    courses = Course.objects.all()
    context = {
        'form': form,
        'student': student,
        'courses': courses
    }
    return render(request, 'edit-student.html', context)


@login_required
@require_http_methods(["POST"])
def delete_student(request, student_id):
    """Delete student"""
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return JsonResponse({'success': True, 'message': 'Student deleted.'})


@login_required
def courses_list(request):
    """Courses list page"""
    courses = Course.objects.annotate(student_count=Count('students')).all()
    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context)


@login_required
@require_http_methods(["POST"])
def add_course(request):
    """Add course"""
    try:
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        
        if not name:
            return JsonResponse({
                'success': False,
                'message': 'Course name is required.'
            })
        
        if Course.objects.filter(name__iexact=name).exists():
            return JsonResponse({
                'success': False,
                'message': 'Course already exists.'
            })
        
        course = Course.objects.create(name=name)
        return JsonResponse({
            'success': True,
            'message': 'Course added.',
            'course': {
                'id': course.id,
                'name': course.name
            }
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        })


@login_required
@require_http_methods(["POST"])
def delete_course(request, course_id):
    """Delete course"""
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return JsonResponse({'success': True, 'message': 'Course deleted.'})


def forgot_password(request):
    """Forgot password page"""
    return render(request, 'forgot.html')


def logout_view(request):
    """Logout page"""
    logout(request)
    return render(request, 'logout.html')


@login_required
def simple_admin(request):
    """Simple admin interface as alternative to Django admin"""
    if not request.user.is_staff:
        messages.error(request, 'You need admin privileges to access this page.')
        return redirect('dashboard')
    
    users = User.objects.all()
    students = Student.objects.select_related('course').all()
    courses = Course.objects.annotate(student_count=Count('students')).all()
    
    context = {
        'users': users,
        'students': students,
        'courses': courses,
        'total_users': users.count(),
        'total_students': students.count(),
        'total_courses': courses.count(),
    }
    return render(request, 'simple-admin.html', context)
