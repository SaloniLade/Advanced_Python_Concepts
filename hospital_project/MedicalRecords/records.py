
def create_record(patient_name, diagnosis, treatment):
    return {
        "patient_name": patient_name,
        "diagnosis": diagnosis,
        "treatment": treatment
    }

def display_record(record):
    print("Patient Name:", record["patient_name"])
    print("Diagnosis:", record["diagnosis"])
    print("Treatment:", record["treatment"])
