# -----------------------------------------------------------
# Name: Luis Rodriguez
# Date: May 17, 2026
# Assignment: Employee and Production Worker Classes
#
# Purpose:
# This program demonstrates inheritance in Python by creating
# Employee and ProductionWorker classes using setters and getters.
#
# Source:
# Original work created for Bellevue University coursework.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Employee Class
# This class stores general employee information.
# -----------------------------------------------------------
class Employee:

    # Constructor method initializes all employee fields
    def __init__(self):

        self.__employee_name = ""
        self.__employee_gender = ""
        self.__employee_hourly_pay_rate = 0.0
        self.__employee_number = ""

    # -------------------------
    # Setter Methods
    # -------------------------

    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_employee_gender(self, employee_gender):
        self.__employee_gender = employee_gender

    def set_employee_hourly_pay_rate(self, hourly_pay_rate):
        self.__employee_hourly_pay_rate = hourly_pay_rate

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

    # -------------------------
    # Getter Methods
    # -------------------------

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_gender(self):
        return self.__employee_gender

    def get_employee_hourly_pay_rate(self):
        return self.__employee_hourly_pay_rate

    def get_employee_number(self):
        return self.__employee_number


# -----------------------------------------------------------
# ProductionWorker Class
# This class inherits from the Employee class and
# adds a shift number field.
# -----------------------------------------------------------
class ProductionWorker(Employee):

    # Constructor method initializes inherited fields
    # and the new shift number field
    def __init__(self):

        Employee.__init__(self)

        self.__shift_number = 0

    # -------------------------
    # Setter Method
    # -------------------------

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    # -------------------------
    # Getter Method
    # -------------------------

    def get_shift_number(self):
        return self.__shift_number


# -----------------------------------------------------------
# Main Function
# Creates objects and displays employee information.
# -----------------------------------------------------------
def main():

    # -------------------------------------------------------
    # Create Employee Objects
    # -------------------------------------------------------

    employee_one = Employee()
    employee_two = Employee()

    # Set values for Employee One
    employee_one.set_employee_name("John Smith")
    employee_one.set_employee_gender("Male")
    employee_one.set_employee_hourly_pay_rate(22.50)
    employee_one.set_employee_number("1")

    # Set values for Employee Two
    employee_two.set_employee_name("Sarah Johnson")
    employee_two.set_employee_gender("Female")
    employee_two.set_employee_hourly_pay_rate(25.75)
    employee_two.set_employee_number("2")

    # -------------------------------------------------------
    # Create Production Worker Objects
    # -------------------------------------------------------

    production_worker_one = ProductionWorker()
    production_worker_two = ProductionWorker()

    # Set values for Production Worker One
    production_worker_one.set_employee_name("Michael Brown")
    production_worker_one.set_employee_gender("Male")
    production_worker_one.set_employee_hourly_pay_rate(28.00)
    production_worker_one.set_employee_number("3")
    production_worker_one.set_shift_number(1)

    # Set values for Production Worker Two
    production_worker_two.set_employee_name("Emily Davis")
    production_worker_two.set_employee_gender("Female")
    production_worker_two.set_employee_hourly_pay_rate(30.25)
    production_worker_two.set_employee_number("4")
    production_worker_two.set_shift_number(3)

    # -------------------------------------------------------
    # Display Employee Information
    # -------------------------------------------------------

    print("=================================================")
    print("               EMPLOYEE INFORMATION              ")
    print("=================================================\n")

    print("Employee One")
    print("---------------------------------------------")
    print("Employee Name: ",
          employee_one.get_employee_name())
    print("Employee Gender: ",
          employee_one.get_employee_gender())
    print("Hourly Pay Rate: $",
          employee_one.get_employee_hourly_pay_rate())
    print("Employee Number: ",
          employee_one.get_employee_number())

    print("\nEmployee Two")
    print("---------------------------------------------")
    print("Employee Name: ",
          employee_two.get_employee_name())
    print("Employee Gender: ",
          employee_two.get_employee_gender())
    print("Hourly Pay Rate: $",
          employee_two.get_employee_hourly_pay_rate())
    print("Employee Number: ",
          employee_two.get_employee_number())

    # -------------------------------------------------------
    # Display Production Worker Information
    # -------------------------------------------------------

    print("\n=================================================")
    print("          PRODUCTION WORKER INFORMATION          ")
    print("=================================================\n")

    print("Production Worker One")
    print("---------------------------------------------")
    print("Employee Name: ",
          production_worker_one.get_employee_name())
    print("Employee Gender: ",
          production_worker_one.get_employee_gender())
    print("Hourly Pay Rate: $",
          production_worker_one.get_employee_hourly_pay_rate())
    print("Employee Number: ",
          production_worker_one.get_employee_number())
    print("Shift Number: ",
          production_worker_one.get_shift_number())

    print("\nProduction Worker Two")
    print("---------------------------------------------")
    print("Employee Name: ",
          production_worker_two.get_employee_name())
    print("Employee Gender: ",
          production_worker_two.get_employee_gender())
    print("Hourly Pay Rate: $",
          production_worker_two.get_employee_hourly_pay_rate())
    print("Employee Number: ",
          production_worker_two.get_employee_number())
    print("Shift Number: ",
          production_worker_two.get_shift_number())


# -----------------------------------------------------------
# Call the main function
# -----------------------------------------------------------
main()