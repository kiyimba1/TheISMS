from django.urls import path

from student_management_app.views import ParentViews,main

parent_url = [
    path('parent_home', ParentViews.parent_home, name="parent_home"),
    path('students', ParentViews.get_students, name="view_students"),
    path('view_notification', ParentViews.parent_all_notification, name="view_notification"),
    # path('results', ParentViews.results, 'results'),
    path('parent_profile', ParentViews.parent_profile, name="parent_profile"),
    path('parent_profile_save', ParentViews.parent_profile_save, name="parent_profile_save"),
    path('parent_fcmtoken_save', ParentViews.parent_fcmtoken_save, name="parent_fcmtoken_save"),
]
