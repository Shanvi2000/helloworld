from django.db import models

class Member(models.Model):
  ROLE_CHOICES = [
    ('manager', 'Manager'),
    ('developer', 'Developer'),
    ('designer', 'Designer'),
    ('hr', 'HR'),
    ('sales', 'Sales'),
    ('support', 'Support'),
    ('intern', 'Intern'),
    ('other', 'Other'),
  ]
  
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(unique=True, null=True, blank=True)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='other')
  working_hours = models.CharField(max_length=50, default='9 AM - 5 PM')
  salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  department = models.CharField(max_length=100, null=True, blank=True)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname} - {self.role}"

