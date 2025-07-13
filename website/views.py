from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Program, Staff_member, Message, Marks_record, ResultDocument
from .forms import AdmissionForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.



def index(request):
    """
    this fnc will render the home page of the site.
    """
    if request.user.is_authenticated:
        # Redirect based on user role
        if request.user.role == 'admin':
            return redirect('admin_view')
        elif request.user.role == 'student':
            return redirect('student_dashboard')
        else:
            programs = Program.objects.all()
            return render(request, 'index.html', {'programs': programs})
    else:
        # If not logged in, show Welcome page
        programs = Program.objects.all()
        return render(request, 'index.html', {'programs': programs})

def programs(request):
    programs = Program.objects.all()
    return render(request, 'programs.html', {'programs': programs})

@login_required
def program_details(request, pk):
    """
    this fnc will find the selected program from database and also handle some admission
    """
    program = get_object_or_404(Program, pk=pk)
    form = AdmissionForm()
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            admit = form.save(commit=False)
            admit.selected_program = program
            enrolled_by = request.user if request.user.is_authenticated else None
            admit.enrolled_by = enrolled_by
            admit.save()
            return render(request, 'admisn_succes.html')
        else:
            print("there is an error in admission")
            return render(request, 'program_detail.html', {'program': program, 'form': form})
    else:
        return render(request, 'program_detail.html', {'program': program,'form': form})

def admission_success(request):
    return render(request, 'admisn_succes.html')

def about(request):
    staff_members = Staff_member.objects.all()
    return render(request, 'aboutUS.html', {'staff_members': staff_members})

# contact view
def contact(request):
    if request.method == 'POST':
        # Handle form submission here
        name = request.POST['username']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Message(name, email, subject, message)
        

    return render(request, 'contact.html')


def show_result(request):
    # Get all marks records
    marks = Marks_record.objects.all()
    rpdf = ResultDocument.objects.first()  # Assuming you want to show the first PDF document
    
    # Group marks by student and program
    results = {}
    for mark in marks:
        student_key = (mark.student.id, mark.program.id)
        if student_key not in results:
            results[student_key] = {
                'student': mark.student,
                'program': mark.program,
                'subjects': {},
                'total_obtained': 0,
                'total_marks': 0,
                'percentage': 0
            }
        results[student_key]['subjects'][mark.subject] = {
            'obtained': mark.obtained_marks,
            'total': mark.total_marks,
            'percentage': (mark.obtained_marks / mark.total_marks) * 100
        }
        results[student_key]['total_obtained'] += mark.obtained_marks
        results[student_key]['total_marks'] += mark.total_marks
    
    # Calculate overall percentage for each student
    for result in results.values():
        if result['total_marks'] > 0:
            result['percentage'] = (result['total_obtained'] / result['total_marks']) * 100

    # Convert dictionary to list for template
    final_results = list(results.values())
    
    return render(request, 'show_result.html', {
        'results': final_results,
        'pdf_url': rpdf.pdf_file.url if rpdf else None
    })

def verify_result(request):
    if request.method == 'POST':
        roll_number = request.POST.get('roll_number')
        session = request.POST.get('session')
        
        # Fetch results based on roll number and session
        marks = Marks_record.objects.filter(student__st_roll_no=roll_number, session=session)
        
        if marks.exists():
            # Group marks by subject
            result = {
                'subjects': {},
                'total_obtained': 0,
                'total_marks': 0,
                'percentage': 0
            }
            for mark in marks:
                result['subjects'][mark.subject] = {
                    'obtained': mark.obtained_marks,
                    'total': mark.total_marks,
                    'percentage': (mark.obtained_marks / mark.total_marks) * 100
                }
                result['total_obtained'] += mark.obtained_marks
                result['total_marks'] += mark.total_marks
            
            # Calculate overall percentage
            if result['total_marks'] > 0:
                result['percentage'] = (result['total_obtained'] / result['total_marks']) * 100
            
            return render(request, 'verify_result.html', {'result': result})
        else:
            messages.error(request, "No results found for the provided roll number and session.")
            return render(request, 'verify_result.html')
    else:
        return render(request, 'verify_result.html')


def verify_certificate(request):
    if request.method == 'POST':
        roll_number = request.POST.get('roll_number')
        registration_number = request.POST.get('registration_number')
        
        # Verify certificate based on roll number or registration number
        certificate = None
        if roll_number:
            certificate = Marks_record.objects.filter(student__roll_number=roll_number).first()
        elif registration_number:
            certificate = Marks_record.objects.filter(student__registration_number=registration_number).first()
        
        if certificate:
            return render(request, 'verify_certificate.html', {'certificate': certificate})
        else:
            messages.error(request, "No certificate found for the provided details.")
            return render(request, 'verify_certificate.html')
    else:
        return render(request, 'verify_certificate.html')