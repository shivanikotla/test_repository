
from cProfile import label
from wsgiref.validate import validator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Interview



def validate_name(name_must):
        if len(name_must)<=4:
            raise ValidationError(
            _('You have enterd "%(value)s" it is too small..! Please Enter Full Name '),
            params={'value': name_must})


# def validate_number(mobile_must):
#     if len(mobile_must)<=10:
#         raise ValidationError(
#             _('You have enterd "%(value)s"..! it should be 10 digits '),
#             params={'value': mobile_must})


class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=50)

class UserForm(forms.ModelForm):
    candidate_name = forms.CharField(label='Candidate Name', validators=[validate_name], widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':' Candidate Name Here'}),max_length=50)# required=True, error_messages={'required':'Must Enter a Correct Candidate Name'}, max_length=50,)
    interviewer_name = forms.CharField(label='Interviewer Name', validators=[validate_name], widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':' Interviewer Name Here'}),max_length=50)# required=True, error_messages={'required':'Must Enter a Correct Interviwer Name'}, max_length=50,)
    mobile = forms.CharField(min_length=10,label='Mobile Number',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Candidate Mobile Number Here'})) #required=True, error_messages={'required':'Must Enter a Mobile Number '})
    email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':' Candidate Email Here'}),min_length=5) #required=True, error_messages={'required':'Must Enter a Correct Email'}, min_length=5)
    date_interview= forms.DateField(label='Date of Interview', widget=forms.SelectDateWidget)
    class Meta:
        model = Interview
        fields = '__all__'
       
        overall_feedback: forms.CharField(label='Feedback',widget=forms.Textarea(attrs={"rows":2, "cols":1, 'placeholder':'Type Feedback Here'}))
        widgets = {
            
            'gender': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'position': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'overall_performance' : forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'programming_fundamentals' : forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'oops_concepts' : forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'framework_concepts' : forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'restful_concepts' : forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'databases' : forms.RadioSelect(attrs={'class': 'form-check-input'}),
            
        }   

        error_messages = {
            'candidate_name' :{'required' : 'Must Enter Candidate Name'},
            'interviewer_name' :{'required': 'Must Enter Interviewer Name'},
            'gender' : { 'required' : 'Must Select a Gender'},
            'email' : { 'required' : 'Enter Correct Email'},
            'mobile' : {'required' : 'Enter a Valid Contact'},
            'position' :{'required' : 'Must selcet position'},
            'overall_performance' :{'required' : 'Must selcet Overall Performance'},
            'overall_performance' :{'required' : 'Must selcet Programming Fundamentals'},
            'oops_concepts' :{'required' : 'Must selcet Opps Concepts'},
            'framework_concepts' :{'required' : 'Must selcet Framework Concepts'},
            'restful_concepts' :{'required' : 'Must selcet Restful_Concepts'},
            'databases' :{'required' : 'Must selcet Databases'},
            
            
           
        }

