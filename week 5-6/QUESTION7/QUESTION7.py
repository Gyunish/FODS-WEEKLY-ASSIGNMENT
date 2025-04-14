import csv
class Employee:
    def __init__(self,empid="",name="",address="",contact_number="",spouse_name="",number_of_child=0,salary=0.0):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary

    def input_details(self):
            print("\nEnter Employee Details:")
            self.empid = input("Enter Employee ID: ")
            self.name = input("Enter Full Name: ")
            self.address = input("Enter Address: ")
            self.contact_number = input("Enter Contact Number: ")
            self.spouse_name = input("Enter Spouse Name (leave blank if not applicable): ")
            self.number_of_child = input("Enter Number of Children: ")
            self.salary = input("Enter Salary: ")

    def to_dict(self):
        return \
        {
            "Employee ID": self.empid,
            "Name": self.name,
            "Address": self.address,
            "Contact Number": self.contact_number,
            "Spouse Name": self.spouse_name,
            "Number of Children": self.number_of_child,
            "Salary": self.salary
        }

    def save_to_csv(self, filename):
        try:
            write_header = False
            try:
                with open(filename, 'r', newline='', encoding='utf-8') as f:
                    pass
            except FileNotFoundError:
                write_header = True

            with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
                fieldnames = ["Employee ID", "Name", "Address", "Contact Number", "Spouse Name", "Number of Children",
                              "Salary"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                if write_header:
                    writer.writeheader()
                writer.writerow(self.to_dict())
                print(f"\nEmployee data saved to '{filename}' successfully.")

        except Exception as e:
            print(f"Error saving to CSV: {e}")

def display_all_employees(filename):
        try:
            file = open(filename, 'r', newline='', encoding='utf-8')
            reader = csv.reader(file)
            rows = list(reader)
            file.close()

            if not rows:
                print("The file is empty.")
                return

            col_widths = [max(len(str(cell)) for cell in col) for col in zip(*rows)]
            separator = '+'.join('-' * (w + 2) for w in col_widths)

            print(separator)
            for row in rows:
                print('| ' + ' | '.join(row[i].ljust(col_widths[i]) for i in range(len(row))) + ' |')
            print(separator)

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error reading CSV: {e}")

emp = Employee()
emp.input_details()
emp.save_to_csv("employees.csv")
display_all_employees("employees.csv")