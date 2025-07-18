# Generated by Django 5.1.7 on 2025-05-28 05:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('duration', models.CharField(help_text='e.g., 3 Months, 6 Months', max_length=50)),
                ('semesters', models.PositiveIntegerField()),
                ('fee', models.DecimalField(decimal_places=2, help_text='Course fee in PKR', max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='course_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Staff_member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='documents/staff-members/')),
                ('description', models.TextField()),
                ('whatsapp_link', models.CharField(max_length=100)),
                ('facebook_link', models.CharField(max_length=100)),
                ('linkdin_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('cnic_number', models.CharField(max_length=15, unique=True)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField()),
                ('highest_qualification', models.CharField(choices=[('Matriculation', 'Matriculation'), ('Intermediate', 'Intermediate'), ('Graduation', 'Graduation'), ('Other', 'Other')], max_length=20)),
                ('year_of_passing_matric', models.PositiveIntegerField()),
                ('matric_institution', models.CharField(max_length=255)),
                ('selected_program', models.CharField(max_length=50)),
                ('scholarship', models.CharField(choices=[('None', 'No'), ('Fully Funded', 'Fully Funded'), ('Partial', 'Partial (50%-70%)')], default='None', max_length=20)),
                ('cnic_copy', models.FileField(blank=True, null=True, upload_to='documents/cnic/')),
                ('passport_photo', models.FileField(blank=True, null=True, upload_to='documents/photos/')),
                ('matric_certificate', models.FileField(blank=True, null=True, upload_to='documents/matric/')),
                ('payment_prof', models.ImageField(upload_to='documents/paymentProf/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('enrolled_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enrolled_applications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('marks', models.IntegerField()),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.program')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('st_roll_no', models.IntegerField(default=0)),
                ('st_reg_no', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('cnic_number', models.CharField(max_length=15)),
                ('contact_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('program', models.CharField(max_length=255)),
                ('highest_qualification', models.CharField(max_length=20)),
                ('year_of_passing_matric', models.PositiveIntegerField()),
                ('matric_institution', models.CharField(max_length=255)),
                ('selected_program', models.CharField(max_length=50)),
                ('scholarship', models.CharField(max_length=20)),
                ('cnic_copy', models.FileField(blank=True, null=True, upload_to='documents/cnic/')),
                ('passport_photo', models.FileField(blank=True, null=True, upload_to='documents/photos/')),
                ('matric_certificate', models.FileField(blank=True, null=True, upload_to='documents/matric/')),
                ('payment_prof', models.ImageField(blank=True, default=' ', null=True, upload_to='documents/paymentProf/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('enrolled_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enrolled_students', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EnrollmentRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled_at', models.DateTimeField(auto_now_add=True)),
                ('enroller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_records', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_records', to='website.student')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.CharField(max_length=255, unique=True)),
                ('issue_date', models.DateField()),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.program')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.student')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_enroller', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
