from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , default=1)

    designation = models.CharField(max_length=255 , null=True, blank=True )


    def __str__(self):
        return f'{self.user.username} '
    

    


class LeaveType(models.Model):
    designation = models.ForeignKey(UserDetails, on_delete=models.CASCADE,null = True)
    leavetype = models.CharField(max_length=255, null=True, blank=True )
    leavename = models.CharField(max_length=255,   null=True, blank=True)
    default_credit = models.IntegerField()

    def __str__(self):
        return f' {self.leavetype}'


class LMS(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE,null=True, blank=True)

    # leavetype = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    leavedays = models.IntegerField()
    reason = models.TextField()


