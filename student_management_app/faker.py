from random import randint
from faker import Faker
from .models import CustomUser, Parents, Students, StudentResult, Term, Staffs
from student_management_app.models import Clss
from django.db.utils import IntegrityError


def students(count=100):
    fake = Faker()
    i = 0
    while i < count:
        try:
            u = CustomUser.objects.create_user(username=fake.user_name(),
                                               email=fake.email(),
                                               first_name=fake.user_name(),
                                               last_name=fake.user_name(),
                                               password='hok', user_type=5
                                               )
            u.students.address = fake.address()
            u.students.nationality = fake.country()
            u.students.term_id = Term.objects.get(id=1)
            u.students.gender = ""
            u.students.gender = ""
            u.students.parent_id = Parents.objects.all()[0]
            i += 1
        except IntegrityError:
            continue


def teachers(count=100):
    fake = Faker()
    i = 0
    while i < count:
        u = CustomUser.objects.create_user(username=fake.user_name(),
                                           email=fake.email(),
                                           first_name=fake.user_name(),
                                           last_name=fake.user_name(),
                                           password='hok', user_type=2
                                           )
        u.staffs.address = fake.address()
        i += 1
