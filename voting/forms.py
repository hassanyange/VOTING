from django import forms
from .models import *
from account.forms import FormSettings 
from .models import College, Department
from django import forms
from .models import College, Department
from django.urls import reverse_lazy

from django import forms
from .models import College, Department

class DepartmentForm(forms.Form):
    college = forms.ModelChoiceField(queryset=College.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_college'}))
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_department'}))






class VoterForm(FormSettings):
    class Meta:
        model = Voter
        fields = ['phone']






class PositionForm(FormSettings):
    class Meta:
        model = Position
        fields = ['name', 'max_vote']


class CandidateForm(FormSettings):
    class Meta:
        model = Candidate
        fields = ['fullname', 'bio', 'position', 'photo']






