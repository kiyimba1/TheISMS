from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse


from student_management_app.models import Payments, PaymentStructure, CustomUser, Term, Clss, Students


def bursar_home(request):
    return render(request, 'bursar_template/home_content.html')


def add_payment(request):
    students = CustomUser.objects.filter(user_type=5)
    sessions = Term.object.all()
    structures = PaymentStructure.objects.all()
    return render(request, "bursar_template/add_payment_template.html",{"students":students, "sessions":sessions,"structures":structures})


def add_payment_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        receipt_number = request.POST.get("receipt_number")
        amount_paid = request.POST.get("amount_paid")
        payment_date = request.POST.get("payment_date")
        student_id = request.POST.get("student")
        structure_id = request.POST.get("structure")
        recorder = CustomUser.objects.get(id=request.user.id)
        student_obj = CustomUser.objects.get(id=student_id)
        structure_obj = PaymentStructure.objects.get(id=structure_id)

        # try:
        p = Payments(
                    student_id=student_obj,
                    added_by = recorder,

                    payment_structure_id=structure_obj,
                    reciept_number=receipt_number,
                    amount_paid=amount_paid,
                    date_paid=payment_date
        )
        p.save()
        messages.success(request, "Successfully Added Payment")
        return HttpResponseRedirect(reverse("manage_payments"))
        # except:
        #     messages.error(request, "Failed to Add Payment")
        #     return HttpResponseRedirect(reverse("add_payment"))


def add_payment_structure(request):
    courses = Clss.objects.all()
    sessions = Term.object.all()
    return render(request, "bursar_template/add_structure_template.html", {"courses": courses, "sessions":sessions})


def add_payment_structure_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        session = request.POST.get("session")
        course = request.POST.get("course")
        amount = request.POST.get("amount")
        code = request.POST.get("code")
        session_obj = Term.object.get(id=session)
        course_obj = Clss.objects.get(id=course)
        user_obj = CustomUser.objects.get(id=request.user.id)

        try:
            p = PaymentStructure(
                    session_id=session_obj,
                    course_id=course_obj,
                    code=code,
                    amount_to_pay=amount,
                    added_by=user_obj,

            )
            p.save()
            messages.success(request, "Successfully Added Payment")
            return HttpResponseRedirect(reverse("manage_structures"))
        except:
            messages.error(request, "Failed to Add Payment")
            return HttpResponseRedirect(reverse("add_structure"))




def manage_structure(request):
    structures = PaymentStructure.objects.all()
    return render(request, 'bursar_template/manage_structure_template.html', {"structures": structures})

def manage_payments(request):
    payments = Payments.objects.all()
    return render(request, 'bursar_template/manage_payment_template.html', {"payments":payments})