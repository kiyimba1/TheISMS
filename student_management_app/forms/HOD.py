from django import forms
from django.forms import ChoiceField

from student_management_app.models import Clss, Term, Parents, CustomUser


class ChoiceNoValidation(ChoiceField):
    def validate(self, value):
        pass


class DateInput(forms.DateInput):
    input_type = "date"


class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, required=False,
                             widget=forms.EmailInput(attrs={"class": "form-control", "autocomplete": "off"}))

    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    nationality = forms.CharField(label="Nationality", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    course_list = []
    try:
        courses = Clss.objects.all()
        for course in courses:
            small_course = (course.id, course.clss_name)
            course_list.append(small_course)
    except:
        course_list = []
    # course_list=[]

    session_list = []
    try:
        sessions = Term.object.all()

        for ses in sessions:
            small_ses = (ses.id, str(ses.term_start_date) +
                         "   TO  " + str(ses.term_end_date))
            session_list.append(small_ses)
    except:
        session_list = []

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    parent_list = []
    #
    try:
        parents = Parents.objects.all()
        for parent in parents:

            small_par = (parent.id, parent.id.first_name +
                         " "+parent.id.last_name)
            parent_list.append(small_par)
    except:
        pass
    parent_id = forms.ChoiceField(label="Parent", choices=parent_list, widget=forms.Select(
        attrs={"class": "form-control"}))

    course = forms.ChoiceField(label="Course", choices=course_list,
                               widget=forms.Select(attrs={"class": "form-control"}))
    sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(
        attrs={"class": "form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_list, required=False,
                                        widget=forms.Select(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", max_length=50,
                                  widget=forms.FileInput(attrs={"class": "form-control"}))


class AddBursarForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, required=False,
                             widget=forms.EmailInput(attrs={"class": "form-control", "autocomplete": "off"}))

    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    nationality = forms.CharField(label="Nationality", max_length=20, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(
        attrs={"class": "form-control"}))

    profile_pic = forms.FileField(label="Profile Pic", max_length=50,
                                  widget=forms.FileInput(attrs={"class": "form-control"}))


class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(
        attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))

    course_list = []
    try:
        courses = Clss.objects.all()
        for course in courses:
            small_course = (course.id, course.clss_name)
            course_list.append(small_course)
    except:
        course_list = []

    session_list = []
    try:
        sessions = Term.object.all()

        for ses in sessions:
            small_ses = (ses.id, str(ses.term_start_date) +
                         "   TO  " + str(ses.term_end_date))
            session_list.append(small_ses)
    except:
        pass
        # session_list = []

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    parent_list = []
    try:
        parents = Parents.objects.all()
        for parent in parents:
            par = CustomUser.objects.get(id=parent.admin_id)
            small_par = (par.id, par.first_name + " " + par.last_name)
            parent_list.append(small_par)
    except:
        pass
    parent_id = forms.ChoiceField(label="Parent", choices=parent_list, widget=forms.Select(
        attrs={"class": "form-control"}))

    course = forms.ChoiceField(label="Course", choices=course_list,
                               widget=forms.Select(attrs={"class": "form-control"}))
    sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(
        attrs={"class": "form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_list,
                                        widget=forms.Select(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", max_length=50,
                                  widget=forms.FileInput(attrs={"class": "form-control"}), required=False)


class AddParentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, required=False,
                             widget=forms.EmailInput(attrs={"class": "form-control", "autocomplete": "off"}))

    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    phone = forms.CharField(label="Phone", max_length=50,
                            widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(
        attrs={"class": "form-control"}))

    profile_pic = forms.FileField(label="Profile Pic", max_length=50,
                                  widget=forms.FileInput(attrs={"class": "form-control"}))


class EditParentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(
        attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(
        attrs={"class": "form-control"}))

    profile_pic = forms.FileField(label="Profile Pic", max_length=50,
                                  widget=forms.FileInput(attrs={"class": "form-control"}), required=False)


class EditBursarForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(
        attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control"}))

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(
        attrs={"class": "form-control"}))

    profile_pic = forms.FileField(label="Profile Pic", max_length=50,
                                  widget=forms.FileInput(attrs={"class": "form-control"}), required=False)
