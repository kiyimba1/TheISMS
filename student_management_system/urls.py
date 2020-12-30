"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import TemplateView

from student_management_app.views import main, HodViews, StaffViews, StudentViews, ParentViews, BursarViews
from student_management_app.views.EditResultVIewClass import EditResultViewClass
from student_management_app.urls import bursar_urls, hod_urls, staff_urls, student_urls, parent_urls


from student_management_system import settings

hod = hod_urls.hod_url

urlpatterns = [

                  path('signup_admin', main.signup_admin, name="signup_admin"),
                  path('signup_student', main.signup_student, name="signup_student"),
                  path('signup_staff', main.signup_staff, name="signup_staff"),
                  path('do_admin_signup', main.do_admin_signup, name="do_admin_signup"),
                  path('do_staff_signup', main.do_staff_signup, name="do_staff_signup"),
                  path('do_signup_student', main.do_signup_student, name="do_signup_student"),
                  path('admin/', admin.site.urls),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('', main.ShowLoginPage, name="show_login"),
                  path('get_user_details', main.GetUserDetails),
                  path('logout_user', main.logout_user, name="logout"),
                  path('doLogin', main.doLogin, name="do_login"),
                  #HOD

                  path('hod/', include(hod_urls.hod_url)),

                  #     Staff URL Path
                  path('staff/', include(staff_urls.staff_url)),


                path('student/', include(student_urls.student_url)),


              #   Parent URLS
                path('parent/', include(parent_urls.parent_url)),

              #   Bursar URLS
                path('bursar/', include(bursar_urls.bursar_url)),


               

                # path('pdf/', HodViews.generate_pdf)

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
