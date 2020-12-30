from django import forms
from django.forms import ChoiceField

from student_management_app.models import Term, Subjects


class ChoiceNoValidation(ChoiceField):
    def validate(self, value):
        pass


class DateInput(forms.DateInput):
    input_type = "date"


class EditResultForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.staff_id = kwargs.pop("staff_id")
        super(EditResultForm, self).__init__(*args, **kwargs)
        subject_list = []
        try:
            subjects = Subjects.objects.filter(staff_id=self.staff_id)
            for subject in subjects:
                subject_single = (subject.id, subject.subject_name)
                subject_list.append(subject_single)
        except:
            subject_list = []
        self.fields['subject_id'].choices = subject_list

    session_list = []
    try:
        sessions = Term.object.all()
        for session in sessions:
            session_single = (session.id, str(session.session_start_year) + " TO " + str(session.session_end_year))
            session_list.append(session_single)
    except:
        session_list = []

    subject_id = forms.ChoiceField(label="Subject", widget=forms.Select(attrs={"class": "form-control"}))
    session_ids = forms.ChoiceField(label="Session Year", choices=session_list,
                                    widget=forms.Select(attrs={"class": "form-control"}))
    student_ids = ChoiceNoValidation(label="Student", widget=forms.Select(attrs={"class": "form-control"}))
    assignment_marks = forms.CharField(label="Assignment Marks",
                                       widget=forms.TextInput(attrs={"class": "form-control"}))
    exam_marks = forms.CharField(label="Exam Marks", widget=forms.TextInput(attrs={"class": "form-control"}))
