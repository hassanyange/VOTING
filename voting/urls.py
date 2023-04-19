from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    # ADDITIONAL URL
    
    path('ballot/fetch/', views.fetch_ballot, name='fetch_ballot'),
    path('dashboard/', views.dashboard, name='voterDashboard'),
    # path('results/', views.view_results, name='voterResults'),
    path('verify/', views.verify, name='voterVerify'),
    path('verify/otp', views.verify_otp, name='verify_otp'),
    path('otp/resend/', views.resend_otp, name='resend_otp'),
    path('ballot/vote', views.show_ballot, name='show_ballot'),
    path('ballot/vote/preview', views.preview_vote, name='preview_vote'),
    path('ballot/vote/submit', views.submit_ballot, name='submit_ballot'),
     path('department_selection/',views.department_selection, name='department_selection'),
]
