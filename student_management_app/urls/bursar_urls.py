from django.urls import path

from student_management_app.views import BursarViews, main

bursar_url = [
    path('', BursarViews.bursar_home, name="bursar_home"),
    path('add_structure', BursarViews.add_payment_structure, name="add_structure"),
    path('add_structure_save', BursarViews.add_payment_structure_save, name="add_structure_save"),
    path('add_payment', BursarViews.add_payment, name="add_payment"),
    path('add_payment_save', BursarViews.add_payment_save, name="add_payment_save"),
    path('manage_structures', BursarViews.manage_structure, name="manage_structures"),
    path('manage_payments', BursarViews.manage_payments, name="manage_payments")
]
