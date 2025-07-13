from django.contrib import admin
from . import models

@admin.action(description='Confirm The Addmission application')
def convert_to_student(modeladmin, request, queryset):
    for admission in queryset:
        student = models.Student(
            full_name = admission.full_name,
            father_name = admission.father_name,
            dob = admission.date_of_birth,
            gender = admission.gender,
            cnic_number = admission.cnic_number,
            contact_number = admission.contact_number,
            email = admission.email,
            address = admission.address,
            program = admission.selected_program,
            highest_qualification = admission.highest_qualification,
            year_of_passing_matric = admission.year_of_passing_matric,
            matric_institution = admission.matric_institution,
            selected_program = admission.selected_program,
            scholarship = admission.scholarship,
            cnic_copy =  admission.cnic_copy,
            passport_photo = admission.passport_photo,
            matric_certificate = admission.matric_certificate,
        payment_prof = admission.payment_prof,
        enrolled_by = admission.enrolled_by
    )
    student.save()
    # Create an enrollment record
    enrollment_record = models.EnrollmentRecord(
        student=student,
        enroller=admission.enrolled_by,
        enrolled_at=admission.created_at if hasattr(admission, 'created_at') else None
    )
    enrollment_record.save()
    
    admission.delete()

class AdmissionAdmin(admin.ModelAdmin):
    actions = [convert_to_student]



# Register your models here.
admin.site.register(models.Program)
admin.site.register(models.Course)
admin.site.register(models.Certificate)
admin.site.register(models.Admission, AdmissionAdmin)
admin.site.register(models.Student)
admin.site.register(models.Staff_member)
admin.site.register(models.Message)
admin.site.register(models.EnrollmentRecord)
admin.site.register(models.Marks_record)
admin.site.register(models.ResultDocument)