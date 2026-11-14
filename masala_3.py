from student import add_student, display_students, search_student
from grades import add_grade, calculate_average_grade, top_student

def main():
    while True:
        print("\n--- Talabalarni Boshqarish Tizimi ---")
        print("1. Talaba qo'shish")
        print("2. Barcha talabalarni ko'rsatish")
        print("3. Ism bo'yicha talaba qidirish")
        print("4. Talabaning bahosini qo'shish")
        print("5. O'rtacha bahoni hisoblash")
        print("6. Eng yuqori baho olgan talabani aniqlash")
        print("0. Chiqish")
        
        choice = input("Tanlovingizni kiriting: ").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            add_grade()
        elif choice == "5":
            calculate_average_grade()
        elif choice == "6":
            top_student()
        elif choice == "0":
            print("Dastur tugatildi.")
            break
        else:
            print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")

if __name__ == "__main__":
    main()