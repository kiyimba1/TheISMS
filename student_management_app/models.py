from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Term(models.Model):
    id = models.AutoField(primary_key=True)
    term_start_date = models.DateField()
    term_end_date = models.DateField()
    term_code = models.CharField(max_length=120)
    objects = models.Manager()

    class Meta:
        db_table = "Term"


class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Bursar"),
                      (4, "Parent"), (5, "Student"))
    user_type = models.CharField(
        default=1, choices=user_type_data, max_length=10)

    class Meta:
        db_table = "User"


class AdminHOD(models.Model):
    id = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.FileField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "Admin"


class Staffs(models.Model):
    id = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    # admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    fcm_token = models.TextField(default="")
    objects = models.Manager()

    class Meta:
        db_table = "Staff"


class Clss(models.Model):
    id = models.AutoField(primary_key=True)
    clss_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "Class"


class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    clss_id = models.ForeignKey(Clss, on_delete=models.CASCADE, default=1)
    staff_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "Subject"


class Parents(models.Model):
    id = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    # admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=8)
    profile_pic = models.FileField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    fcm_token = models.TextField(default="")
    objects = models.Manager()

    class Meta:
        db_table = "Parent"


class PaymentStructure(models.Model):
    id = models.AutoField(primary_key=True)

    term_id = models.ForeignKey(Term, on_delete=models.DO_NOTHING)
    clss_id = models.ForeignKey(Clss, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=12)
    amount_to_pay = models.CharField(max_length=12)
    last_updated = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    objects = models.Manager()

    class Meta:
        db_table = "PaymentStructure"


class Students(models.Model):
    id = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    # admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=24)
    gender = models.CharField(max_length=255)
    profile_pic = models.FileField()
    address = models.TextField()
    clss_id = models.ForeignKey(Clss, on_delete=models.DO_NOTHING)
    parent_id = models.ForeignKey(Parents, on_delete=models.DO_NOTHING)
    term_id = models.ForeignKey(Term, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    fcm_token = models.TextField(default="")
    objects = models.Manager()

    class Meta:
        db_table = "Student"


class Payments(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    added_by = models.ForeignKey(
        CustomUser, on_delete=models.DO_NOTHING, related_name='added_by')
    payment_structure_id = models.ForeignKey(
        PaymentStructure, on_delete=models.DO_NOTHING)
    reciept_number = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=12)
    balance = models.CharField(max_length=12, blank=True, null=True)
    date_paid = models.DateTimeField()
    date_recorded = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "Payment"


class Bursar(models.Model):
    id = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    # admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=12)
    profile_pic = models.FileField()
    address = models.TextField()
    objects = models.Manager()

    class Meta:
        db_table = "Bursar"


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "Attendance"


class AttendanceReport(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "AttendanceReport"


class LeaveReportStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "StudentLeaveReport"


class LeaveReportStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "StaffLeaveReport"


class FeedBackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "StudentFeedBack"


class FeedBackParent(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.ForeignKey(Parents, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "ParentFeedBack"


class FeedBackStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.DO_NOTHING)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "StaffFeedBack"


class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "StudentNotification"


class NotificationStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "StaffNotification"


class StudentResult(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    subject_exam_marks = models.FloatField(default=0)
    term_id = models.ForeignKey(Term, on_delete=models.CASCADE)
    aggregate = models.CharField(max_length=50)
    remark = models.CharField(max_length=150)
    initails = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    subject_assignment_marks = models.FloatField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "Result"


class OnlineClassRoom(models.Model):
    id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=255)
    room_pwd = models.CharField(max_length=255)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    terms = models.ForeignKey(Term, on_delete=models.CASCADE)
    started_by = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "OnlineClass"


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminHOD.objects.create(id=instance)
        if instance.user_type == 2:
            Staffs.objects.create(id=instance, address="")
        if instance.user_type == 3:
            Bursar.objects.create(id=instance)
        if instance.user_type == 4:
            Parents.objects.create(id=instance)
        if instance.user_type == 5:
            Students.objects.create(id=instance, clss_id=Clss.objects.get(id=1),
                                    term_id=Term.objects.get(id=1), address="", profile_pic="",
                                    gender="", parent_id=Parents.objects.get(id=1))


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 3:
        instance.bursar.save()
    if instance.user_type == 4:
        instance.parents.save()
    if instance.user_type == 5:
        instance.students.save()
