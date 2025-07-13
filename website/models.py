from django.db import models
from accounts.models import CustomUser

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_enroller = models.BooleanField(default=False)

class Program(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=50, help_text="e.g., 3 Months, 6 Months")
    semesters = models.PositiveIntegerField()
    fee = models.DecimalField(max_digits=10, decimal_places=2, help_text="Course fee in PKR")
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"
    

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    marks = models.IntegerField()
    

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    full_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    dob = models.DateField()
    st_roll_no = models.IntegerField(default=0)
    st_reg_no = models.CharField(max_length=50)

    gender = models.CharField(max_length=10)
    cnic_number = models.CharField(max_length=15)
    contact_number = models.CharField(max_length=20) 

    email = models.EmailField()
    address = models.TextField()
    program = models.CharField(max_length=255)

    highest_qualification = models.CharField(max_length=20)
    year_of_passing_matric = models.PositiveIntegerField()
    matric_institution = models.CharField(max_length=255)
    enrolled_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='enrolled_students')

    selected_program = models.CharField(max_length=50)
    scholarship = models.CharField(max_length=20)
    cnic_copy = models.FileField(upload_to='documents/cnic/', blank=True, null=True)

    passport_photo = models.FileField(upload_to='documents/photos/', blank=True, null=True)
    matric_certificate = models.FileField(upload_to='documents/matric/', blank=True, null=True)
    payment_prof = models.ImageField(upload_to="documents/paymentProf/", blank=True, null=True, default=" ")

    # Submission Date
    submitted_at = models.DateTimeField(auto_now_add=True)
    # registrartion number

    def __str__(self):
        return f'{self.full_name}'



class Admission(models.Model):
    # Personal Details
    GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ]

    full_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    cnic_number = models.CharField(max_length=15, unique=True)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()

    # Educational Background
    QUALIFICATION_CHOICES = [
    ('Matriculation', 'Matriculation'),
    ('Intermediate', 'Intermediate'),
    ('Graduation', 'Graduation'),
    ('Other', 'Other'),
    ]

    highest_qualification = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES)
    year_of_passing_matric = models.PositiveIntegerField()
    matric_institution = models.CharField(max_length=255)

    # Course Selection
    selected_program = models.CharField(max_length=50)
    
    # Scholarship Details
    SCHOLARSHIP_CHOICES = [
    ('None', 'No'),
    ('Fully Funded', 'Fully Funded'),
    ('Partial', 'Partial (50%-70%)'),
    ]

    scholarship = models.CharField(max_length=20, choices=SCHOLARSHIP_CHOICES, default='None')

    # Attachments
    cnic_copy = models.FileField(upload_to='documents/cnic/', blank=True, null=True)
    passport_photo = models.FileField(upload_to='documents/photos/', blank=True, null=True)
    matric_certificate = models.FileField(upload_to='documents/matric/', blank=True, null=True)
    payment_prof = models.ImageField(upload_to="documents/paymentProf/", blank=False, null=False)

    # Submission Date
    submitted_at = models.DateTimeField(auto_now_add=True)

    # enrolled by enroller
    enrolled_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='enrolled_applications')

    # str representation
    def __str__(self):
        return f'Application of {self.full_name}, S or D/O {self.father_name}'

    # if fees is submmited then we will accept thier application and convert them into student
    def convert_to_student(self):
        student = models.Student(
                full_name = self.full_name,
                father_name = self.father_name,
                dob = self.date_of_birth,
                gender = self.gender,
                cnic_number = self.cnic_number,
                contact_number = self.contact_number,
                email = self.email,
                address = self.address,
                program = self.program,
                highest_qualification = self.highest_qualification,
                year_of_passing_matric = self.year_of_passing_matric,
                matric_institution = self.matric_institution,
                selected_program = self.selected_program,
                scholarship = self.scholarship,
                cnic_copy =  self.cnic_copy,
                passport_photo = self.passport_photo,
                matric_certificate = self.matric_certificate,
                payment_prof = self.payment_prof
            )
        student.save()
        self.delete()

class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    certificate_number = models.CharField(max_length=255, unique=True)
    issue_date = models.DateField()


class Staff_member(models.Model):
    name = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    image = models.ImageField(upload_to="documents/staff-members/", blank=False, null=False)
    description = models.TextField()
    whatsapp_link = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length=100)
    linkdin_link = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Message(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"The message {self.subject} by {self.username}"

class EnrollmentRecord(models.Model):
    enroller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='enrollment_records')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollment_records')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} enrolled by {self.enroller.username} on {self.enrolled_at.strftime('%Y-%m-%d')}"
    


class Marks_record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks_record')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='marks_records')
    subject = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='marks_record')
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField()

    def __str__(self):
        return f"{self.student} is enrolled in {self.program}, in the subject {self.subject}, obtained {self.obtained_marks} marks in {self.total_marks}"
    


class ResultDocument(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='Resultpdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title