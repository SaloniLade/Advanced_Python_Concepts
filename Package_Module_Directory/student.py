
def total_marks(marks):
    return sum(marks)

def percentage(marks, maximum_per_subject=100):
    maximum = len(marks) * maximum_per_subject
    if maximum == 0:
        return 0
    return (sum(marks) / maximum) * 100

def grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 75:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 40:
        return "D"
    else:
        return "Fail"
