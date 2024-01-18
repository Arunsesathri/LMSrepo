from django.forms import ModelChoiceField,CharField ,IntegerField
# from django.forms import ModelForm, ValidationError

from django import forms
# from .models import leave_applications
from django.contrib import admin
from .models import UserDetails

from .models import LeaveType

from .models import LMS




class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = '__all__'  # You can specify the fields you want to include here 



class Leavetypeform(forms.ModelForm):
    class Meta:
        model = LeaveType
        fields = '__all__'  # You can specify the fields you want to include here

        # fields = ['designation', 'leavetype', 'leavename', 'default_credit']


    # def __init__(self, *args, **kwargs):
    #     super(Leavetypeform, self).__init__(*args, **kwargs)
    #     # Get unique designations and create choices for the dropdown
    #     unique_designations = UserDetails.objects.values_list('designation', flat=True).distinct()
    #     designation_choices = [(designation, designation) for designation in unique_designations]
    #     self.fields['designation'].widget = forms.Select(choices=designation_choices)



class Leavesform(forms.ModelForm):
    class Meta:
        model = LMS
        fields = ['leave_type', 'start_date', 'end_date', 'leavedays','reason']

    widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
    leave_type = ModelChoiceField(queryset=LeaveType.objects.all(), empty_label=None)
      


