# appname/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('sample1/', views.sample, name='sample1'),
    path('user/', views.user1, name='user'),
    path('addingleavetype/', views.leavetype1, name='addingleavetype'),
    # path('leaveforms/', views.leaves, name='leaveforms'),
    path('userdetails_list/', views.userdetails_list, name='userdetails_list'),
    
    
    path('leaveforms/<int:user_id>/', views.leaves, name='leaveforms'),


# Correct URL pattern with 'username' and 'designation'
    # path('leaveforms/<int:user_id>/<int:leavetype_id>/', views.leaves, name='leaveforms'),
    # path('leaveforms/<int:user_id>/<int:leavetype_id>/', views.leaves, name='leaveforms'),

    path('success', views.success, name='success'),

    # Add more paths for your app's views here
]



