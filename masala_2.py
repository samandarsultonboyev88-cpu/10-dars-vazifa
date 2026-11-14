from student import load_data, save_data

def add_grade():
    name = input("Baho qo'shiladigan talabaning ismi: ").strip().lower()
    students = load_data()
    for student in students:
        if student["name"].lower() == name:
            try:
                grade = float(input("Talabaning bahosini kiriting: "))
                student["grades"].append(grade)
                save_data(students)
                print("Baho muvaffaqiyatli qo'shildi!")
                return
            except ValueError:
                print("Xato: Faqat raqam kiriting!")
                return
    print("Talaba topilmadi.")

def calculate_average_grade():
    name = input("O'rtacha bahosi hisoblanadigan talabaning ismi: ").strip().lower()
    students = load_data()
    for student in students:
        if student["name"].lower() == name:
            grades = student["grades"]
            if not grades:
                print("Bu talabaning baholari yo'q.")
                return
            avg = sum(grades) / len(grades)
            print(f"{student['name']} ning o'rtacha bahosi: {avg:.2f}")
            return
    print("Talaba topilmadi.")

def top_student():
    students = load_data()
    if not students:
        print("Talabalar mavjud emas.")
        return
    
    best_student = None
    max_avg = -1
    
    for student in students:
        grades = student["grades"]
        if grades:
            avg = sum(grades) / len(grades)
            if avg > max_avg:
                max_avg = avg
                best_student = student["name"]
                
    if best_student:
        print(f"Eng yuqori o'rtacha baho olgan talaba: {best_student} ({max_avg:.2f})")
    else:
        print("Hozircha hech kimda baholar yo'q.")