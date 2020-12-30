from django import forms
from django.forms import ChoiceField

from student_management_app.models import Students, PaymentStructure, CustomUser, Clss, Term

class DateInput(forms.DateInput):
    input_type = "date"

class AddPaymentForm(forms.Form):
    reciept_number = forms.CharField(label="Reciept Number", widget=forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}))
    amount_paid = forms.CharField(label="Amount Paid", widget=forms.TextInput(attrs={"class":"form-control", "autocomplete":"off"}))
    payment_date = forms.DateField(label="Date of Payment", widget=forms.DateInput(attrs={"class":"form-control", "data-target":"#datetimepicker1","data-toggle":"datetime-picker"}))

    student_list = []
    try:
        students = Students.objects.all()
        for student in students:
            std = CustomUser.objects.get(id=student.admin_id)
            small_student = (std.id, std.first_name+" "+std.last_name)
            student_list.append(small_student)
    except:
        pass
        # student_list = []
    student_id = forms.ChoiceField(label="Student", choices=student_list,widget=forms.Select(attrs={"class": "form-control"}))

    structure_list = []
    try:
        strc = PaymentStructure.objects.all()
        for structure in strc:
            small_structure = (structure.payment_structure_id, structure.code)
            structure_list.append(small_structure)
    except:
        pass
    structure_id = forms.ChoiceField(label="Structure", choices=structure_list, widget=forms.Select(attrs={"class": "form-control"}))

class AddPaymentStructureForm(forms.Form):
    course_list = []
    try:
        courses = Clss.objects.all()
        for course in courses:
            small_course = (course.id, course.course_name)
            course_list.append(small_course)
    except:
        course_list = []

    session_list = []
    try:
        sessions = Term.object.all()

        for ses in sessions:
            small_ses = (ses.id, str(ses.session_start_year) + "   TO  " + str(ses.session_end_year))
            session_list.append(small_ses)
    except:
        pass
        # session_list = []

    session_id = forms.ChoiceField(label="Sessoin", choices=session_list,widget=forms.Select(attrs={"class": "form-control"}))
    course_id = forms.ChoiceField(label="Course", choices=course_list,widget=forms.Select(attrs={"class": "form-control"}))
    amount_to_pay = forms.CharField(label="Amount To Be Paid", widget=forms.TextInput(attrs={"class":"form-control"}))
    code = forms.CharField(label="Code", widget=forms.TextInput(attrs={"class": "form-control"}))