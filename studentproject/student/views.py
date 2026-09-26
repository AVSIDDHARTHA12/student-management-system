from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student, Marks


def add_student(request):
    if request.method == "POST":
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        age = request.POST.get('age')
        course = request.POST.get('course')

        Student.objects.create(
            roll=roll,
            name=name,
            age=age,
            course=course,
        )
        return redirect('add_marks')

    return render(request, 'add_student.html')


def add_marks(request):
    if request.method == "POST":
        roll = request.POST.get('roll')
        telugu = request.POST.get('telugu')
        english = request.POST.get('english')
        maths = request.POST.get('maths')
        science = request.POST.get('science')

        try:
            student = Student.objects.get(roll=roll)
            Marks.objects.update_or_create(
                student=student,
                defaults={
                    'telugu': telugu,
                    'english': english,
                    'maths': maths,
                    'science': science,
                }
            )
            return redirect('view_student')
        except Student.DoesNotExist:
            return render(request, 'add_marks.html', {'error': f"Student with roll number '{roll}' does not exist."})

    return render(request, 'add_marks.html')


def view_student(request):
    student = None
    marks = None
    error = None

    if request.method == "POST":
        roll = request.POST.get('roll')
        try:
            student = Student.objects.get(roll=roll)
            marks = Marks.objects.filter(student=student).first()
        except Student.DoesNotExist:
            error = f"No student found with Roll Number '{roll}'."

    return render(request, 'view_student.html', {
        'student': student,
        'marks': marks,
        'error': error
    })


def edit_details(request, roll):
    student = get_object_or_404(Student, roll=roll)
    marks = Marks.objects.filter(student=student).first()

    if request.method == "POST":
        # Update Student fields
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.course = request.POST.get('course')
        student.save()

        # Update or create Marks fields
        telugu = request.POST.get('telugu')
        english = request.POST.get('english')
        maths = request.POST.get('maths')
        science = request.POST.get('science')

        if any([telugu, english, maths, science]):
            Marks.objects.update_or_create(
                student=student,
                defaults={
                    'telugu': telugu or 0,
                    'english': english or 0,
                    'maths': maths or 0,
                    'science': science or 0,
                }
            )

        return redirect('view_student')

    return render(request, 'edit_details.html', {
        'student': student,
        'marks': marks,
    })