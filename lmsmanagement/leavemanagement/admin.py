from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.


# myapp/admin.py
from django.contrib import admin
from .models import UserDetails

from .models import LeaveType
from .models import LMS




# these are the steps of linesto get in userid field no. incerasing automatically
class CustomUserAdmin(UserAdmin):
    list_display = ('user_id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')

    def user_id(self, obj):
        return obj.id
    user_id.short_description = 'User ID'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserDetails)
admin.site.register(LeaveType)
admin.site.register(LMS)

