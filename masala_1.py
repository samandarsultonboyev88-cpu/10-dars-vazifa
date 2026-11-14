import json
import os

FILE_NAME = "students.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_student():
    name = input("Talabaning ismi: ").strip()
    students = load_data()
    for student in students:
        if student["name"].lower() == name.lower():
            print("Bu talaba allaqachon mavjud!")
            return
    students.append({"name": name, "grades": []})
    save_data(students)
    print("Talaba muvaffaqiyatli qo'shildi!")

def display_students():
    students = load_data()
    if not students:
        print("Hozircha talabalar yo'q.")
        return
    print("\n--- Talabalar ro'yxati ---")
    for i, student in enumerate(students, 1):
        print(f"{i}. Ism: {student['name']} | Baholar: {student['grades']}")

def search_student():
    name = input("Qidirilayotgan talabaning ismi: ").strip().lower()
    students = load_data()
    found = False
    for student in students:
        if name in student["name"].lower():
            print(f"Topildi -> Ism: {student['name']}, Baholar: {student['grades']}")
            found = True
    if not found:
        print("Talaba topilmadi.")