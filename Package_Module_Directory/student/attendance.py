
def attendance_eligibility(attended, total):
    if total <= 0 or attended < 0 or attended > total:
        return "Invalid attendance data"

    percent = (attended / total) * 100

    if percent >= 75:
        return "Eligible"
    return "Not eligible"
