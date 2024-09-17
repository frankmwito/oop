# employee management system

class Employee:
    def __init__(self):
        self.employees = []  # List to store employee details
    
    def add_employee(self):
        """Add a new employee to the system."""
        num_of_employees = int(input("Enter the number of employees to add: "))
        for i in range(num_of_employees):
            name = input(f"Enter the name of employee {i + 1}: ")
            emp_id = input(f"Enter the ID of employee {i + 1}: ")
            salary = float(input(f"Enter the salary of employee {i + 1}: "))
            employee = {"name": name, "ID": emp_id, "salary": salary}
            self.employees.append(employee)
        print(f"Successfully added {num_of_employees} employees.")

    def remove_employee(self, emp_id):
        """Remove an employee by ID."""
        employee_found = False
        for employee in self.employees:
            if employee["ID"] == emp_id:
                self.employees.remove(employee)
                employee_found = True
                print(f"Employee with ID {emp_id} has been removed.")
                break
        if not employee_found:
            print(f"Employee with ID {emp_id} not found.")

    def get_employee_info(self, emp_id):
        """Get the details of an employee by ID."""
        employee_found = False
        for employee in self.employees:
            if employee["ID"] == emp_id:
                print(f"Employee details: Name: {employee['name']}, ID: {employee['ID']}, Salary: {employee['salary']}")
                employee_found = True
                break
        if not employee_found:
            print(f"Employee with ID {emp_id} not found.")


# Example usage
employee_management = Employee()

# Adding employees
employee_management.add_employee()

# Displaying information of an employee
emp_id_to_search = input("Enter the employee ID to search for details: ")
employee_management.get_employee_info(emp_id_to_search)

# Removing an employee
emp_id_to_remove = input("Enter the employee ID to remove: ")
employee_management.remove_employee(emp_id_to_remove)

# Displaying the remaining employees
print("Updated list of employees:")
for emp in employee_management.employees:
    print(emp)
