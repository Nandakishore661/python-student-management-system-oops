class student:
    def __init__(self, id , name , age , place):
        self.id = id
        self.name = name
        self.age = age
        self.place = place
    
    def display_details(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Place:",self.place)
        
class StudentManagement:
    def __init__(self):
        self.students = []
        
    def add_student(self):
        id = int(input("enter student ID:"))
        
        for i in self.students:
            if i.id == id:
               print("Student ID Already Exists!")
               return
        
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        place = input("Enter Student Place: ")

        s = student(id, name, age, place)
        
        self.students.append(s)
        
        print("student added successfully..")
        
    # View All Students
    def view_all_students(self):
        if len(self.students) == 0:
            print("No Student Available..")
        
        else:
            for i in self.students:
                print("-------------")
                i.display_details()
                
    # Search Student
    def search_student(self):
        id  = int(input("enter a student ID:"))
        
        for i in self.students:
            if i.id == id:
                print("student found..")
                i.display_details()
                return
        print("student not found..")
        
     # Update Student
    def update_student(self):
        id = int(input("enter student ID to Update:"))
        
        for i in self.students:
            if i.id == id:
                i.name = input("Enter New Name: ")
                i.age = int(input("Enter New Age: "))
                i.place = input("Enter New Place: ")

                print("Student Updated Successfully!")
                return 
        print("student not found..")
        
     # Delete Student
    def delete_student(self):
        id = int(input("enter student ID to delete:"))
        
        for i in self.students:
            if i.id == id:
                self.students.remove(i)
                print("Student Deleted Successfully!")
                return

        print("Student Not Found!")
        
# Main Program

obj = StudentManagement()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    
    choice = int(input("enter your choice:"))
    
    if choice == 1:
        obj.add_student()
        
    elif choice == 2:
        obj.view_all_students()
    
    elif choice == 3:
        obj.search_student()
        
    elif choice == 4:
        obj.update_student()
    
    elif choice == 5:
        obj.delete_student()
    
    elif choice == 6:
        print("Thank You!")
        break
    
    else:
        print("Invalid Choice!")
        