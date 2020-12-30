from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from student_management_app.models import Students, AttendanceReport, LeaveReportStudent, CustomUser, Parents


def parent_home(request):
    parent = Parents.objects.get(admin_id=request.user.id)
    student_count1 = Students.objects.filter(parent_id=parent.admin_id)

    my_students = Students.objects.filter(parent_id=parent)
    attendance_present_list_student = []
    attendance_absent_list_student = []
    student_name_list = []
    for student in my_students:
        attendance = AttendanceReport.objects.filter(student_id=student.id, status=True).count()
        absent = AttendanceReport.objects.filter(student_id=student.id, status=False).count()
        leaves = LeaveReportStudent.objects.filter(student_id=student.id, leave_status=1).count()
        attendance_present_list_student.append(attendance)
        attendance_absent_list_student.append(leaves + absent)
        student_name_list.append(student.admin.username)

    print(student_count1, student_name_list)
    return render(request, "parent_template/home_content.html",
                  {"student_count": student_count1,  "student_name_list": student_name_list,
                   "attendance_present_list_student": attendance_present_list_student,
                   "attendance_absent_list_student": attendance_absent_list_student})


@csrf_exempt
def parent_fcmtoken_save(request):
    token = request.POST.get("token")
    try:
        parent = Parents.objects.get(admin=request.user.id)
        parent.fcm_token = token
        parent.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

def parent_all_notification(request):
    parent = Parents.objects.get(admin=request.user.id)
    notifications = NotificationParent.objects.filter(parent_id=parent.id)
    return render(request, "parent_template/all_notification.html", {"notifications": notifications})

def parent_view_result(request, student_id):
    student = Students.objects.get(admin=student_id)
    studentresult = StudentResult.objects.filter(student_id=student.id)
    return render(request, "parent_template/student_result.html", {"studentresult": studentresult})


def parent_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    parent = Parents.objects.get(admin=user)
    return render(request, "parent_template/parent_profile.html", {"user": user, "parent": parent})


def parent_profile_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("parent_profile"))
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()

            parent = Parents.objects.get(admin=customuser)
            parent.address = address
            parent.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("parent_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("parent_profile"))


@csrf_exempt
def get_students(request):
    subject_id = request.POST.get("subject")
    session_year = request.POST.get("session_year")

    subject = Subjects.objects.get(id=subject_id)
    session_model = SessionYearModel.object.get(id=session_year)
    students = Students.objects.filter(course_id=subject.course_id, session_year_id=session_model)
    list_data = []

    for student in students:
        data_small = {"id": student.admin.id, "name": student.admin.first_name + " " + student.admin.last_name}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)

@csrf_exempt
def get_attendance_dates(request):
    subject = request.POST.get("subject")
    session_year_id = request.POST.get("session_year_id")
    subject_obj = Subjects.objects.get(id=subject)
    session_year_obj = SessionYearModel.object.get(id=session_year_id)
    attendance = Attendance.objects.filter(subject_id=subject_obj, session_year_id=session_year_obj)
    attendance_obj = []
    for attendance_single in attendance:
        data = {"id": attendance_single.id, "attendance_date": str(attendance_single.attendance_date),
                "session_year_id": attendance_single.session_year_id.id}
        attendance_obj.append(data)

    return JsonResponse(json.dumps(attendance_obj), safe=False)

@csrf_exempt
def parent_fcmtoken_save(request):
    token = request.POST.get("token")
    try:
        parent = Parents.objects.get(admin=request.user.id)
        parent.fcm_token = token
        parent.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")


def parent_all_notification(request):
    parent = Parents.objects.get(admin=request.user.id)
    notifications = NotificationStaffs.objects.filter(parent_id=parent.id)
    return render(request, "parent_template/all_notification.html", {"notifications": notifications})
