from django.contrib import admin

from .models import *

admin.site.register(Candidate)
admin.site.register(College)
admin.site.register(Voter)
admin.site.register(Votes)
admin.site.register(Position)
admin.site.register(Admin)
admin.site.register(Department)


