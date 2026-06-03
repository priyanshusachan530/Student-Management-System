import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anshu@2006",
    database="student_db"
)
cur = conn.cursor()

def add_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    phone = input("Enter Phone Number: ")
    cur.execute(
        "INSERT INTO students VALUES (%s,%s,%s,%s,%s)",
        (sid, name, age, course, phone)
    )
    conn.commit()
    print("Student Added Successfully")

def view_students():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    print("ID | Name | Age | Course | Phone")
    for r in rows:
        print(r)

def update_student():
    sid = int(input("Enter Student ID: "))
    phone = input("Enter New Phone Number: ")
    cur.execute(
        "UPDATE students SET phone=%s WHERE student_id=%s",
        (phone, sid)
    )
    conn.commit()
    print("Student Updated Successfully")

def search_student():
    sid = int(input("Enter Student ID: "))
    cur.execute("SELECT * FROM students WHERE student_id=%s", (sid,))
    row = cur.fetchone()
    if row:
        print(row)
    else:
        print("Student Not Found")

def delete_student():
    sid = int(input("Enter Student ID: "))
    cur.execute("DELETE FROM students WHERE student_id=%s", (sid,))
    conn.commit()
    print("Student Deleted")

while True:
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Update Student")
    print("4.Search Student")
    print("5.Delete Student")
    print("6.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        add_student()
    elif ch == 2:
        view_students()
    elif ch == 3:
        update_student()
    elif ch == 4:
        search_student()
    elif ch == 5:
        delete_student()
    elif ch == 6:
        break


conn.close()
