# AttendX Login Test

def test_login():
    username = "student01"
    password = "valid123"

    if username == "student01" and password == "valid123":
        print("PASS: Login successful")
    else:
        print("FAIL: Login unsuccessful")


def test_invalid_login():
    username = "student01"
    password = "wrong123"

    if username == "student01" and password != "valid123":
        print("PASS: Invalid login rejected")
    else:
        print("FAIL: Invalid login accepted")


if __name__ == "__main__":
    test_login()
    test_invalid_login()