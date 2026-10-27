
def total_marks(marks):
    return sum(marks)

def percentage(marks, maximum=100):
    if not marks:
        return 0
    return (sum(marks) / (len(marks) * maximum)) * 100
