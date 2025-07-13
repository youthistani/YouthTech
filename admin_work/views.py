from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from website import models
from website import forms
from django.contrib.auth.models import User

# Create your views here.
def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

@login_required
def admin_view(req):
    """
    This function will render the admin dashboard with all the necessary data.
    It will display the number of programs, courses, admission applications, staff members, and students.
    It will also provide links to manage programs, courses, and applications.
    """
    program = models.Program.objects.all()
    course = models.Course.objects.all()
    admission_applications = models.Admission.objects.all()
    staff_member = models.Staff_member.objects.all()
    student = models.Student.objects.all()
    

    return render(req, 'admin_dashboard.html', 
                  {
                      'programs': program,
                      'courses': course,
                      'applications': admission_applications,
                      'staff_members': staff_member,
                      'students': student,
                  }
                )

@user_passes_test(is_admin)
def admin_programs(request):
    """
    This function will render the admin programs page.
    It will display all the programs in the database.
    """
    programs = models.Program.objects.all()
    return render(request, 'admin_programs.html', {'programs': programs})

@user_passes_test(is_admin)
def program_create(request):
    """This function will handle the creation of a new program.
    It will render a form to create a new program and save it to the database.
    It will also handle the validation of the form data."""
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        duration = request.POST.get('duration')
        fee = request.POST.get('fee')
        semesters = request.POST.get('semesters')
        if name:
            models.Program.objects.create(name=name, description=description, image=image,
                                   duration=duration, fee=fee, semesters=semesters)
            messages.success(request, 'Program created successfully.')
            return redirect('admin_view')
        else:
            messages.error(request, 'Name is required.')
            return render(request, 'program_create.html')

@user_passes_test(is_admin)
def program_update(request, pk):
    """
    This function will handle the update of an existing program.
    It will render a form to update the program details and save the changes to the database.
    It will also handle the validation of the form data.
    """
    program = get_object_or_404(models.Program, pk=pk)
    if request.method == 'POST':
        program.name = request.POST.get('name')
        program.description = request.POST.get('description')
        program.image = request.FILES.get('image', program.image)
        program.duration = request.POST.get('duration')
        program.fee = request.POST.get('fee')
        program.semesters = request.POST.get('semesters')
        program.save()
        messages.success(request, 'Program updated successfully.')
        return redirect('admin_view')
    return render(request, 'program_update.html', {'program': program})

@user_passes_test(is_admin)
def program_delete(request, pk):
    """This function will handle the deletion of an existing program.
    It will render a confirmation page before deleting the program from the database.
    It will also handle the deletion of the program and display a success message.
    """
    program = get_object_or_404(models.Program, pk=pk)
    if request.method == 'POST':
        program.delete()
        messages.success(request, 'Program deleted successfully.')
        return redirect('admin_view')
    return render(request, 'program_delete_confirm.html', {'program': program})

# --- Course CRUD Views ---

@user_passes_test(is_admin)
def admin_courses(request):
    """This function will render the admin courses page.
    It will display all the courses in the database.
    It will also provide links to create, update, and delete courses.
    """
    courses = models.Course.objects.all()
    return render(request, 'admin_courses.html', {'courses': courses})

@user_passes_test(is_admin)
def course_create(request):
    """This function will handle the creation of a new course.
    It will render a form to create a new course and save it to the database.
    It will also handle the validation of the form data."""
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        program_id = request.POST.get('program')
        program = models.Program.objects.get(pk=program_id) if program_id else None
        marks = request.POST.get('marks')
        
        if name and program:
            models.Course.objects.create(
                name=name,
                description=description,
                program=program,
                marks=marks,
                )
            messages.success(request, 'Course created successfully.')
            return redirect('admin_view')
        else:
            messages.error(request, 'Name and Program are required.')
            return render(request, 'course_create.html', {'programs': models.Program.objects.all()})
    return render(request, 'course_create.html', {'programs': models.Program.objects.all()})

@user_passes_test(is_admin)
def course_update(request, pk):
    """This function will handle the update of an existing course.
    It will render a form to update the course details and save the changes to the database.
    It will also handle the validation of the form data.""" 

    course = get_object_or_404(models.Course, pk=pk)
    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.description = request.POST.get('description')
        program_id = request.POST.get('program')
        course.program = models.Program.objects.get(pk=program_id) if program_id else course.program
        course.duration = request.POST.get('duration')
        course.fee = request.POST.get('fee')
        course.save()
        messages.success(request, 'Course updated successfully.')
        return redirect('admin_view')
    return render(request, 'course_update.html', {'course': course, 'programs': models.Program.objects.all()})

@user_passes_test(is_admin)
def course_delete(request, pk):
    """This function will handle the deletion of an existing course.
    It will render a confirmation page before deleting the course from the database.
    It will also handle the deletion of the course and display a success message.
    """
    course = get_object_or_404(models.Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course deleted successfully.')
        return redirect('admin_view')
    return render(request, 'course_delete_confirm.html', {'course': course})

# --- Application CRUD Views ---

@user_passes_test(is_admin)
def admin_applications(request):
    """This function will render the admin applications page.
    It will display all the admission applications in the database.
    It will also provide links to create, update, and delete applications.
    """
    applications = models.Admission.objects.all()
    return render(request, 'admin_applications.html', {'applications': applications})

@user_passes_test(is_admin)
def application_create(request):
    """This function will handle the creation of a new admission application.
    It will render a form to create a new application and save it to the database.
    It will also handle the validation of the form data.
    """
    programs = models.Program.objects.all()
    if request.method == 'POST':
        form = forms.AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            program = form.cleaned_data.get('program')
            form.instance.program = program
            form.save()
            messages.success(request, 'Application created successfully.')
            return redirect('admin_applications')
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'application_create.html', {'form': form})
    else:
        form = forms.AdmissionForm()
    return render(request, 'application_create.html', {
        'form': form,
        'programs': programs
    })

@user_passes_test(is_admin)
def application_update(request, pk):
    """This function will handle the update of an existing admission application.
    It will render a form to update the application details and save the changes to the database.
    It will also handle the validation of the form data.
    """
    application = get_object_or_404(models.Admission, pk=pk)
    if request.method == 'POST':
        form = forms.AdmissionForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application updated successfully.')
            return redirect('admin_applications')
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'application_update.html', {'form': form, 'application': application})
    else:
        form = forms.AdmissionForm(instance=application)
    return render(request, 'application_update.html', {'form': form, 'application': application})

@user_passes_test(is_admin)
def application_delete(request, pk):
    """This function will handle the deletion of an existing admission application.
    It will render a confirmation page before deleting the application from the database.
    It will also handle the deletion of the application and display a success message.
    """
    application = get_object_or_404(models.Admission, pk=pk)
    if request.method == 'POST':
        application.delete()
        messages.success(request, 'Application deleted successfully.')
        return redirect('admin_applications')
    return render(request, 'application_delete_confirm.html', {'application': application})




# --- Upload Result pdf view ---
@user_passes_test(is_admin)
def upload_result_pdf(request, pk):
    """This function will handle the upload of result PDF files.
    It will render a form to upload the PDF file and save it to the database.
    It will also handle the validation of the form data.
    """
    if request.method == 'POST':
        form = forms.ResultUploadForm(request.POST, request.FILES)
        if form.is_valid():
            result_pdf = form.save(commit=False)
            result_pdf.uploaded_by = request.user
            result_pdf.save()
            messages.success(request, 'Result PDF uploaded successfully.')
            return redirect('admin_view')
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'upload_result_pdf.html', {'form': form})
    else:
        form = forms.ResultUploadForm()
    return render(request, 'upload_result_pdf.html', {'form': form})

