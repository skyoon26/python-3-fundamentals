# Need to import the Employee class in order for the Company class to have access to it
# The lowercase employee is the file name and the uppercase Employee is the class name
from employee import Employee


class Company:
    def __init__(self):
        # No parameters but initialize a property called employees
        # This empty list will be used for storing Employee objects for the Company
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print("Current Employees:")
        for i in self.employees:
            print(i.first_name, i.last_name)
        print("----------------------------")

    def pay_employees(self):
        print("Paying Employees:")
        for i in self.employees:
            print("Paycheck for:", i.first_name, i.last_name)
            # An 'f' string allows you to add variables to a string with curly brackets
            # Inside the curly brackets after the value you want to print, you add a colon
            # To the right of the colon you add the format that you want
            # ',' means thousands get separated by a comma
            # '.2f' means we want floats rounded to 2 decimal places
            print(f"Amount: ${i.calculate_paycheck():,.2f}")
            print("----------------------------")


def main():
    my_company = Company()

    employee1 = Employee("Deanne", "Chae", 50000)
    my_company.add_employee(employee1)

    employee2 = Employee("Bob", "Jones", 25000)
    my_company.add_employee(employee2)

    employee2 = Employee("Frank", "Smith", 60000)
    my_company.add_employee(employee2)

    my_company.display_employees()
    my_company.pay_employees()


main()
