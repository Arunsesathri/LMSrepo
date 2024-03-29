from django.shortcuts import render
from .models import LeaveType, LMS

# Create your views here.
# appname/views.py
from django.shortcuts import render
from django.http import HttpResponse

def sample(request):
    return HttpResponse("Hello, this is my app's view!")


def success(request):
    return render(request, 'success.html')

# myapp/views.py
from django.shortcuts import render
from .models import UserDetails

# def user1(request):
#     if request.method == 'POST':
#         user_id = request.POST['user_id']
#         designation_id = request.POST['designation_id']

#         UserDetails.objects.create(user_id=user_id, designation_id=designation_id)

#     return render(request, 'users.html')




from .forms import UserDetailsForm

def user1(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('userdetails_list')  # Redirect to a success page or another view
    else:
        form = UserDetailsForm()

    return render(request, 'users.html', {'form': form})




from .forms import Leavetypeform




def leavetype1(request):
    if request.method == 'POST':
        form = Leavetypeform(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('userdetails_list')  # Redirect to a success page or another view
    else:
        form = Leavetypeform()

    return render(request, 'leavetype.html', {'form': form})




from .forms import Leavesform


# def leaves(request):
#     if request.method == 'POST':
#         form = Leavesform(request.POST)
#         if form.is_valid():
#             form.save()
#             # return redirect('userdetails_list')  # Redirect to a success page or another view
#     else:
#         form = Leavesform()

#     return render(request, 'leaveapply.html', {'form': form})


# have this
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import LMS

# def leaves(request, user_id):
#     user = get_object_or_404(User, id=user_id)

#     if request.method == 'POST':
#         form = Leavesform(request.POST)
#         if form.is_valid():
#             # Save the form data
#             form.save()
#             # Add any additional logic or redirect as needed
#             return redirect('leaves', user_id=user.id)
#     else:
#         form = Leavesform()

#     return render(request, 'leaveapply.html', {'user': user, 'form': form})








def  userdetails_list(request):
     user_details = UserDetails.objects.all()
     return render(request, 'getusersdetails.html', {'user_details': user_details})




from django.contrib.auth.models import User  # Add this import statement

from django.shortcuts import render, get_object_or_404
from .models import LMS  # Make sure this import is correct


# def leaves(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     leave_types = LeaveType.objects.all()

#     # Create a dictionary to store availed leaves and balance days for each leave type
#     leave_data = {}

#     for leave_type in leave_types:
#         availed_leaves = LMS.objects.filter(user=user, leave_type=leave_type)
#         availed_days = sum(leave.leavedays for leave in availed_leaves)
#         balance_days = leave_type.default_credit - availed_days

#         leave_data[leave_type] = {
#             'availed_leaves': availed_leaves,
#             'balance_days': balance_days,
#         }

#     if request.method == 'POST':
#         form = Leavesform(request.POST)
#         if form.is_valid():
#             # Associate the user and leave type with the form before saving
#             form.instance.user = user
#             form.save()

#             # Redirect to success page
#             return redirect('success')  # Replace 'success' with the name of your success URL

#     else:
#         form = Leavesform()

#     context = {
#         'user': user,
#         'leave_data': leave_data,
#         'form': form,
#     }

#     return render(request, 'leaveapply.html', context)


# this is coprrect

from django.shortcuts import render, get_object_or_404, redirect
from .models import LMS, LeaveType
from .forms import Leavesform

def leaves(request, user_id):
    user = get_object_or_404(User, id=user_id)
    leave_types = LeaveType.objects.all()

    # Create a dictionary to store availed leaves and balance days for each leave type
    leave_data = {}

    for leave_type in leave_types:
        availed_leaves = LMS.objects.filter(user=user, leave_type=leave_type)
        availed_days = sum(leave.leavedays for leave in availed_leaves)
        balance_days = leave_type.default_credit - availed_days

        leave_data[leave_type] = {
            'availed_leaves': availed_leaves,
            'balance_days': balance_days,
            'total_availed_days': availed_days,  # Add total availed days for each leave type
        }

    if request.method == 'POST':
        form = Leavesform(request.POST)
        if form.is_valid():
            # Associate the user and leave type with the form before saving
            form.instance.user = user
            form.save()

            # Redirect to success page
            return redirect('success')  # Replace 'success' with the name of your success URL

    else:
        form = Leavesform()

    context = {
        'user': user,
        'leave_data': leave_data,
        'form': form,
    }

    return render(request, 'leaveapply.html', context)
