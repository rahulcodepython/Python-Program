import csv


class TablePrinter:
    def __init__(self, array_of_objects, width_list=[15, 30, 3, 3, 3, 3, 3, 3, 3], condition=None):
        self.array_of_objects = array_of_objects
        self.headers = list(array_of_objects[0].__dict__.keys())
        self.width_list = width_list
        self.condition = condition or (lambda x: True)
        self.count = 0

    def print_table(self):
        if array_of_objects:
            row_format = (
                f"| "
                + " ".join([f"{{:<{i}}} |" for i in self.width_list])
            )

            line_length = sum(self.width_list) + 3 * len(self.width_list) + 1

            print("-" * line_length)
            print(row_format.format(*self.headers))
            print("-" * line_length)

            for obj in array_of_objects:
                if self.condition(obj):
                    self.count += 1
                    values = [str(obj.__dict__.get(header, ""))
                              for header in self.headers]
                    print(row_format.format(*values))
                    print("-" * line_length)

            print(f"Number of records: {self.count}")
        else:
            print("No data found in the CSV file.")


class DataObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def csv_to_array_of_objects(file_path):
    array_of_objects = []
    with open(file_path, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            array_of_objects.append(DataObject(**row))
    return array_of_objects


def get_values():
    student_code = int(input("Enter student code: "))
    assignment_submission_array = []

    all_submitted = input("All assignments submitted? (y/n): ")
    if all_submitted == "y":
        assignment_submission_array = ["Y"] * 7
        return [student_code, assignment_submission_array]

    consicutive_submitted = input(
        "Are the assignments submitted consecutively? (y/n): "
    )
    if not (consicutive_submitted == "n"):
        number_of_assignments = int(
            input("Enter number of assignments submitted: "))
        assignment_submission_array = ["Y"] * number_of_assignments
        return [student_code, assignment_submission_array]

    for i in range(7):
        answer = input(f"Enter assignment {i+1} submission: ")
        if answer == "y":
            assignment_submission_array.append("Y")
        else:
            assignment_submission_array.append("")

    return [student_code, assignment_submission_array]


def value_insert(array_of_objects, student_code, assignment_submission_array):
    for object in array_of_objects:
        obj = object.__dict__
        if obj["Student Code"] == f"BWU/BCA/23/{student_code}":
            for i, element in enumerate(assignment_submission_array):
                index = str(i + 1)
                if element == "Y":
                    obj[index] = "Y"
            break


def update_file(file_path, array_of_objects):
    with open(file_path, mode="w") as csv_file:
        fieldnames = array_of_objects[0].__dict__.keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for obj in array_of_objects:
            writer.writerow(obj.__dict__)


def print_array_of_objects_in_table(array_of_objects):
    table_printer = TablePrinter(
        array_of_objects=array_of_objects)
    table_printer.print_table()


def print_array_of_objects_in_table_searched_by_student_code(array_of_objects):
    student_code = int(input("Enter student code: "))

    def find_student(obj):
        return obj.__dict__.get("Student Code", "") == f"BWU/BCA/23/{student_code}"

    table_printer = TablePrinter(
        array_of_objects=array_of_objects, condition=find_student)
    table_printer.print_table()


def print_no_student(array_of_objects):
    print(f"Number of students without student code: {len(array_of_objects)}")


def print_array_of_objects_in_table_seached_by_no_submissions(array_of_objects):
    def find_student_not_submitted(obj):
        return all(obj.__dict__.get(str(i), "") == "" for i in range(1, 8))

    table_printer = TablePrinter(
        array_of_objects=array_of_objects, condition=find_student_not_submitted)
    table_printer.print_table()


def print_array_of_objects_in_table_seached_by_assignment_no(array_of_objects):
    while True:
        x = int(input("Enter the number of assignment (1-7): "))
        if 1 <= x <= 7:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 7.")

    def find_student_not_submitted_no(obj):
        return obj.__dict__.get(str(x), "") != "Y"

    table_printer = TablePrinter(
        array_of_objects=array_of_objects, condition=find_student_not_submitted_no)
    table_printer.print_table()


if __name__ == "__main__":
    file_path = "BCA2023_G.csv"  # Replace with your CSV file path
    array_of_objects = csv_to_array_of_objects(file_path)

    while True:
        print("Enter 1 to update the file.")
        print("Enter 2 to print in table format.")
        print("Enter 3 to print in table format of a student.")
        print("Enter 4 to print the number of students in our section.")
        print(
            "Enter 5 to print the number of students who aren't submitted any one of those assignments."
        )
        print(
            "Enter 6 to print the number of students who aren't submitted x assignments."
        )
        print("7 to exit.")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            student_code, assignment_submission_array = get_values()
            value_insert(array_of_objects, student_code,
                         assignment_submission_array)
            update_file(file_path, array_of_objects)
        elif choice == 2:
            print_array_of_objects_in_table(array_of_objects)
        elif choice == 3:
            print_array_of_objects_in_table_searched_by_student_code(
                array_of_objects)
        elif choice == 4:
            print_no_student(array_of_objects)
        elif choice == 5:
            print_array_of_objects_in_table_seached_by_no_submissions(
                array_of_objects)
        elif choice == 6:
            print_array_of_objects_in_table_seached_by_assignment_no(
                array_of_objects)
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")
