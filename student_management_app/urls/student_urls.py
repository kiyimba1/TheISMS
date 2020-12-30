from django.urls import path

from student_management_app.views import StudentViews,main, StaffViews

student_url = [
                  path('', StudentViews.student_home, name="student_home"),
                  path('student_view_attendance', StudentViews.student_view_attendance, name="student_view_attendance"),
                  path('student_view_attendance_post', StudentViews.student_view_attendance_post,
                       name="student_view_attendance_post"),
                  path('student_apply_leave', StudentViews.student_apply_leave, name="student_apply_leave"),
                  path('student_apply_leave_save', StudentViews.student_apply_leave_save,
                       name="student_apply_leave_save"),
                  path('student_feedback', StudentViews.student_feedback, name="student_feedback"),
                  path('student_feedback_save', StudentViews.student_feedback_save, name="student_feedback_save"),
                  path('student_profile', StudentViews.student_profile, name="student_profile"),
                  path('student_profile_save', StudentViews.student_profile_save, name="student_profile_save"),
                  path('student_fcmtoken_save', StudentViews.student_fcmtoken_save, name="student_fcmtoken_save"),
                  path('firebase-messaging-sw.js', main.showFirebaseJS, name="show_firebase_js"),
                  path('student_all_notification', StudentViews.student_all_notification,
                       name="student_all_notification"),
                  path('student_view_result', StudentViews.student_view_result, name="student_view_result"),
                  path('join_class_room/<int:subject_id>/<int:session_year_id>', StudentViews.join_class_room,
                       name="join_class_room"),
                  path('node_modules/canvas-designer/widget.html', StaffViews.returnHtmlWidget,
                       name="returnHtmlWidget"),
                  path('testurl/', main.Testurl),
]