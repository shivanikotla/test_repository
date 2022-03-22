from typing_extensions import Required
from django.db import models


# Create your models here.
class Interview(models.Model):
    candidate_name = models.CharField(max_length=100, null=True, blank=True)
    interviewer_name = models.CharField(max_length=100, null=True, blank=True)
    date_interview = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=20,null=True, blank=True)
    

    
    DEPARTMENTS = (
        ('Java Developer', 'Java Developer'),
        ('Python Delveloper', 'Python Delveloper'),
        ('UI/UX Developer', 'UI/UX Developer'),
        ('.NET Developer', '.NET Developer'),
        ('iOS Developer', 'iOS Developer'),
    )
    position = models.CharField(max_length=100, default=None, choices=DEPARTMENTS)
    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDERS, null=True, default=None)
    overall_feedback = models.TextField(null=True, blank=True)
    overall_perfrmance_choices = (
        ('5- Exceptional', '5- Exceptional'),
        ('4- Above Average', '4- Above Average'),
        ('3- Average', '3- Average'),
        ('2- Satisfactory', '2- Satisfactory'),
        ('1- Unsatisfactory', '1- Unsatisfactory')
    )

    overall_performance= models.CharField(max_length=100, default=None,choices=overall_perfrmance_choices)
    programming_fundamentals = models.CharField(max_length=100, default=None,choices=overall_perfrmance_choices)
    oops_concepts = models.CharField(max_length=100, default=None,choices=overall_perfrmance_choices)
    framework_concepts = models.CharField(max_length=100,default=None,choices=overall_perfrmance_choices)
    restful_concepts = models.CharField(max_length=100,default=None,choices=overall_perfrmance_choices)
    databases = models.CharField(max_length=100, default=None, choices=overall_perfrmance_choices)
    

    def __str__(self):
        return self.candidate_name
   

    
