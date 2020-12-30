from random import randrange
import datetime

current_date = datetime.date.today()
current_year = current_date.year


def student_number_generator(nationality, course_id, session_id):
    std = randrange(0, 9999, 4)
    if (nationality == "UG") | (nationality == "Uganda"):
        nat = "U"
    else:
        nat = "I"
    num = str(nat) + str(current_year) + str(course_id) + str(session_id) + str(std)
    return num

def staff_number_generator():
    stf = randrange(100, 9999, 4)
    num = str("ST")+str(current_year)+str(stf)
    return num

def parent_number_generator():
    stf = randrange(100, 9999, 4)
    num = str("P")+str(current_year)+str(stf)
    return num