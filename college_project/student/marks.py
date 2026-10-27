
def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks):
    if not marks:
        return 0
    return sum(marks) / (len(marks) * 100) * 100
