import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("students.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll INTEGER UNIQUE NOT NULL,
    marks REAL
)
""")

conn.commit()

# -----------------------------
# Functions for CRUD operations
# -----------------------------

def add_student(name, roll, marks):
    try:
        cursor.execute("INSERT INTO students (name, roll, marks) VALUES (?, ?, ?)", (name, roll, marks))
        conn.commit()
        print("✅ Student added successfully!")
    except sqlite3.IntegrityError:
        print("⚠️ Roll number must be unique. Student not added.")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n📋 All Students:")
    for row in rows:
        print(row)

def update_marks(roll, new_marks):
    cursor.execute("UPDATE students SET marks = ? WHERE roll = ?", (new_marks, roll))
    conn.commit()
    if cursor.rowcount == 0:
        print("⚠️ No student found with that roll number.")
    else:
        print("✅ Marks updated successfully!")

def delete_student(roll):
    cursor.execute("DELETE FROM students WHERE roll = ?", (roll,))
    conn.commit()
    if cursor.rowcount == 0:
        print("⚠️ No student found with that roll number.")
    else:
        print("🗑️ Student deleted successfully!")

# -----------------------------
# Menu-driven system
# -----------------------------
while True:
    print("\n=== Student Database Menu ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        roll = int(input("Enter roll number: "))
        marks = float(input("Enter marks: "))
        add_student(name, roll, marks)

    elif choice == '2':
        view_students()

    elif choice == '3':
        roll = int(input("Enter roll number to update: "))
        new_marks = float(input("Enter new marks: "))
        update_marks(roll, new_marks)

    elif choice == '4':
        roll = int(input("Enter roll number to delete: "))
        delete_student(roll)

    elif choice == '5':
        print("👋 Exiting program. Goodbye!")
        break

    else:
        print("❌ Invalid choice, please try again.")

# Close the connection when done
conn.close()
