# class student with methods to add grades and calculate the average grade

class student:
    def __init__(self, name):
        self.name = name
        self.grades = []
        
    def average_grade(self):
        subjects = int(input("Enter the size of grades list: "))
        
        for i in range(subjects):
            self.grades.append(float(input(f"Enter the grades at {i+1}: ")))
            
        sum = 0
        for grade in self.grades:
            sum += grade
            
        average = sum/len(self.grades)
        
        print(f"{self.name} your average grade is: {average}")
        
        
student1 = student(input("Enter your name: "))

student1.average_grade()