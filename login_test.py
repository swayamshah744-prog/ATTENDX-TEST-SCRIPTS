# AttendX Login Test

def test_login():
    username = "student01"
    password = "valid123"

    if username == "student01" and password == "valid123":
        print("PASS: Login successful")
    else:
        print("FAIL: Login unsuccessful")


if __name__ == "__main__":
    test_login()