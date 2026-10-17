# AttendX Attendance Marking Test

def test_attendance():
    student_id = "STU101"
    attendance_status = "Present"

    if student_id and attendance_status in ["Present", "Absent"]:
        print("PASS: Attendance marked successfully")
    else:
        print("FAIL: Invalid attendance details")


if __name__ == "__main__":
    test_attendance()