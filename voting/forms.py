from django import forms
from .models import *
from account.forms import FormSettings 
from django import forms
from django.urls import reverse_lazy
from .models import EvaluationForm




class VoterForm(FormSettings):
    class Meta:
        model = Voter
        fields = ['phone']


class AdminForm(FormSettings):
    class Meta:
        model = Admin
        fields = ['phone']





class PositionForm(FormSettings):
    class Meta:
        model = Position
        fields = ['name', 'max_vote']


class CandidateForm(FormSettings):
    class Meta:
        model = Candidate
        fields = ['fullname', 'bio', 'position', 'photo']






