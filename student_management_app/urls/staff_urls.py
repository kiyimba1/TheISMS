from django.urls import path

from student_management_app.views import StaffViews,main
from student_management_app.views.EditResultVIewClass import EditResultViewClass

staff_url = [
                  path('', StaffViews.staff_home, name="staff_home"),
                  path('staff_take_attendance', StaffViews.staff_take_attendance, name="staff_take_attendance"),
                  path('staff_update_attendance', StaffViews.staff_update_attendance, name="staff_update_attendance"),
                  path('get_students', StaffViews.get_students, name="get_students"),
                  path('get_attendance_dates', StaffViews.get_attendance_dates, name="get_attendance_dates"),
                  path('get_attendance_student', StaffViews.get_attendance_student, name="get_attendance_student"),
                  path('save_attendance_data', StaffViews.save_attendance_data, name="save_attendance_data"),
                  path('save_updateattendance_data', StaffViews.save_updateattendance_data,
                       name="save_updateattendance_data"),
                  path('staff_apply_leave', StaffViews.staff_apply_leave, name="staff_apply_leave"),
                  path('staff_apply_leave_save', StaffViews.staff_apply_leave_save, name="staff_apply_leave_save"),
                  path('staff_feedback', StaffViews.staff_feedback, name="staff_feedback"),
                  path('staff_feedback_save', StaffViews.staff_feedback_save, name="staff_feedback_save"),
                  path('staff_profile', StaffViews.staff_profile, name="staff_profile"),
                  path('staff_profile_save', StaffViews.staff_profile_save, name="staff_profile_save"),
                  path('staff_fcmtoken_save', StaffViews.staff_fcmtoken_save, name="staff_fcmtoken_save"),
                  path('staff_all_notification', StaffViews.staff_all_notification, name="staff_all_notification"),
                  path('staff_add_result', StaffViews.staff_add_result, name="staff_add_result"),
                  path('save_student_result', StaffViews.save_student_result, name="save_student_result"),
                  path('edit_student_result', EditResultViewClass.as_view(), name="edit_student_result"),
                  path('fetch_result_student', StaffViews.fetch_result_student, name="fetch_result_student"),
                  path('start_live_classroom', StaffViews.start_live_classroom, name="start_live_classroom"),
                  path('start_live_classroom_process', StaffViews.start_live_classroom_process,
                       name="start_live_classroom_process"),
]