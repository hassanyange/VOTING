from django.db import models
from account.models import CustomUser
from django import forms
# Create your models here.

class College(models.Model):
    name = models.CharField(max_length= 80)
    location_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100 )
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class Voter(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, unique=True)  # Used for OTP
    otp = models.CharField(max_length=10, null=True)
    verified = models.BooleanField(default=False)
    voted = models.BooleanField(default=False)
    otp_sent = models.IntegerField(default=0)  # Control how many OTPs are sent
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.admin.last_name + ", " + self.admin.first_name
    
class Admin(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, unique=True)  # Used for OTP
    otp = models.CharField(max_length=10, null=True) 
    verified = models.BooleanField(default=False)
    voted = models.BooleanField(default=False)
    otp_sent = models.IntegerField(default=0)  # Control how many OTPs are sent
    department = models.ForeignKey(Department,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.admin.last_name + ", " + self.admin.first_name


class Position(models.Model):
    name = models.CharField(max_length=50, unique=True)
    max_vote = models.IntegerField()
    priority = models.IntegerField()
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    fullname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="candidates")
    bio = models.TextField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class Votes(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)


# class EvaluationForm(forms.Form):
#     def __init__(self, candidates, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for candidate in candidates:
#             prefix = f'candidate_{candidate.id}'
#             self.fields[f'{prefix}_leadership'] = forms.IntegerField(min_value=1, max_value=10, required=True)
#             self.fields[f'{prefix}_managerial'] = forms.IntegerField(min_value=1, max_value=10, required=True)
#             self.fields[f'{prefix}_public_relations'] = forms.IntegerField(min_value=1, max_value=10, required=True)
#             self.fields[f'{prefix}_academic_leadership'] = forms.IntegerField(min_value=1, max_value=10, required=True)
#             department = models.ForeignKey(Department, on_delete=models.CASCADE)
# class Evaluation(models.Model):
#     leadership_ability = models.IntegerField(null=True)
#     managerial_ability = models.IntegerField(null=True)
#     publicRelations_ability = models.IntegerField(null=True)
#     academic_ability = models.IntegerField(null=True)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)