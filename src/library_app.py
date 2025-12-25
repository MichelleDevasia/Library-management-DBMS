import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mySql@123",
        database="library_db"
    )

def list_books():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT book_id, book_title FROM BOOK")
    rows = cur.fetchall()
    print("\n--- Books ---")
    for r in rows:
        print(r[0], "-", r[1])
    cur.close()
    conn.close()
    pause()

def add_member():
    member_id = int(input("Member ID: "))
    name = input("Name: ")
    dept = input("Department: ")
    phone = input("Phone: ")
    email = input("Email: ")
    join_date = input("Join date (YYYY-MM-DD): ")

    conn = get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO MEMBER VALUES (%s, %s, %s, %s, %s, %s)"
    data = (member_id, name, dept, phone, email, join_date)
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()
    print("Member added successfully.")
    pause()

def add_book():
    book_id = int(input("Book ID: "))
    title = input("Title: ")
    isbn = input("ISBN: ")
    category = input("Category: ")
    price = float(input("Price: "))
    publisher_id = int(input("Publisher ID: "))

    conn = get_connection()
    cur = conn.cursor()
    sql = """INSERT INTO BOOK (book_id, book_title, isbn, category, price, publisher_id)
             VALUES (%s, %s, %s, %s, %s, %s)"""
    data = (book_id, title, isbn, category, price, publisher_id)
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()
    print("Book added.")
    pause()

def issue_book():
    issue_id = int(input("Issue ID: "))
    member_id = int(input("Member ID: "))
    book_id = int(input("Book ID: "))
    employee_id = int(input("Employee ID: "))
    issue_date = input("Issue date (YYYY-MM-DD): ")

    conn = get_connection()
    cur = conn.cursor()

    # 1) Check member exists
    cur.execute("SELECT 1 FROM MEMBER WHERE member_id = %s", (member_id,))
    if cur.fetchone() is None:
        print("Member not found. Please add the member first.")
        cur.close()
        conn.close()
        pause()
        return

    # 2) Check book exists
    cur.execute("SELECT 1 FROM BOOK WHERE book_id = %s", (book_id,))
    if cur.fetchone() is None:
        print("Book not found. Please add the book first.")
        cur.close()
        conn.close()
        pause()
        return

    # 3) Check employee exists
    cur.execute("SELECT 1 FROM EMPLOYEE WHERE employee_id = %s", (employee_id,))
    if cur.fetchone() is None:
        print("Employee not found.")
        cur.close()
        conn.close()
        pause()
        return

    # 4) If all exist, insert ISSUE
    sql = """INSERT INTO ISSUE (issue_id, issue_date, return_date,
                                member_id, book_id, employee_id)
             VALUES (%s, %s, NULL, %s, %s, %s)"""
    data = (issue_id, issue_date, member_id, book_id, employee_id)
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()
    print("Book issued successfully.")
    pause()


def list_issues():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT i.issue_id, m.name, b.book_title, i.issue_date, i.return_date
        FROM ISSUE i
        JOIN MEMBER m ON i.member_id = m.member_id
        JOIN BOOK b   ON i.book_id = b.book_id
    """)
    print("\n--- Issues ---")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
    pause()

def pause():
    input("\nPress Enter to continue...")

def main_menu():
    while True:
        print("\n--- Library Menu ---")
        print("1. List all books")
        print("2. Add member")
        print("3. Add book")
        print("4. Issue book")
        print("5. List issued books")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            list_books()
        elif choice == "2":
            add_member()
        elif choice == "3":
            add_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            list_issues()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")



if __name__ == "__main__":
    main_menu()

