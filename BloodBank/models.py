from django.db import models
from django.utils import timezone

# Donor: info about blood donors


# Choices for blood groups
BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]

class Donor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    age = models.PositiveIntegerField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    last_donation_date = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.blood_group})"
    
    def is_eligible_for_donation(self):
        """ Check if the donor is eligible to donate. For example, donors can donate every 80 days. """
        if not self.is_available:
            return False
        if self.last_donation_date:
            days_since_last_donation = (date.today() - self.last_donation_date).days
            return days_since_last_donation >= 80  # Assuming donors can donate every 80 days
        return True

