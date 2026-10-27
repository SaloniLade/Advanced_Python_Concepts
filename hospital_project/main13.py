# 14. Create a project directory containing packages for: 
# a) Patient management  b) Doctor management  c) Billing  d) Medical records  
# Implement simple functions in each module and access them from main.py. 


from Patient.patient_details import get_patient
from Doctor.doctor_details import get_doctor
from Billing.bill import calculate_bill, display_bill
from MedicalRecords.records import create_record, display_record

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

doctor_name = input("Enter doctor name: ")
specialization = input("Enter specialization: ")

diagnosis = input("Enter diagnosis: ")
treatment = input("Enter treatment: ")

patient = get_patient(name, age)
doctor = get_doctor(doctor_name, specialization)

record = create_record(name, diagnosis, treatment)

print("\n--- Patient Information ---")
print("Name:", patient["name"])
print("Age:", patient["age"])

print("\n--- Doctor Information ---")
print("Doctor:", doctor["name"])
print("Specialization:", doctor["specialization"])

print("\n--- Medical Record ---")
display_record(record)

print("\n--- Billing Information ---")
consultation = float(input("Consultation fee: Rs. "))
medicine = float(input("Medicine cost: Rs. "))
tests = float(input("Test cost: Rs. "))

if min(consultation, medicine, tests) < 0:
    print("Costs cannot be negative.")
else:
    total = calculate_bill(consultation, medicine, tests)
    display_bill(total)
