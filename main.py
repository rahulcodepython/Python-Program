from tabulate import tabulate
import csv


class TablePrinter:
    def __init__(
        self,
        data,
        column_widths=[30, 15, 3, 3, 3, 3, 3, 3, 3],
        conditional_formatting=None,
    ):
        """
        Initializes the TablePrinter with data, headers, optional column widths, and conditional formatting.

        :param data: List of dictionaries containing the data to be displayed.
        :param headers: List of column headers.
        :param column_widths: Optional list of integers specifying the width of each column.
        :param conditional_formatting: Optional list of tuples (condition_func, format_func).
        """
        self.data = data
        self.headers = list(data[0].__dict__.keys())
        self.column_widths = column_widths
        self.conditional_formatting = conditional_formatting or []

    def _apply_conditional_formatting(self, row):
        """
        Applies conditional formatting to a row based on the provided conditions.

        :param row: Dictionary representing a single row of data.
        :return: Formatted row as a list of strings.
        """
        formatted_row = []
        for header in self.headers:
            cell_value = str(row.get(header, ""))
            for condition_func, format_func in self.conditional_formatting:
                if condition_func(header, cell_value):
                    cell_value = format_func(cell_value)
            formatted_row.append(cell_value)
        return formatted_row

    def _truncate_data(self):
        """
        Truncates data based on the specified column widths.
        """
        if not self.column_widths:
            return self.data

        truncated_data = []
        for row in self.data:
            truncated_row = {}
            for header, width in zip(self.headers, self.column_widths):
                cell_data = str(row.get(header, ""))
                if len(cell_data) > width:
                    truncated_row[header] = cell_data[: width - 3] + "..."
                else:
                    truncated_row[header] = cell_data
            truncated_data.append(truncated_row)
        return truncated_data

    def print_table(self):
        """
        Prints the table with the specified formatting and conditional formatting.
        """
        truncated_data = self._truncate_data()
        table_data = [self._apply_conditional_formatting(row) for row in truncated_data]
        print(tabulate(table_data, headers=self.headers, tablefmt="grid"))


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


def print_array_of_objects(array_of_objects):
    for obj in array_of_objects:
        print(obj.__dict__)


def print_array_of_objects_in_table(array_of_objects):
    table_printer = TablePrinter(array_of_objects)
    table_printer.print_table()
    # if array_of_objects:
    #     headers = list(array_of_objects[0].__dict__.keys())
    #     name_header = "Name"
    #     student_code_header = "Student Code"
    #     other_headers = [
    #         header
    #         for header in headers
    #         if header not in [name_header, student_code_header]
    #     ]

    #     name_width = 30
    #     student_code_width = 15
    #     other_width = 3  # 1 space on each side + 3 for the value
    #     row_format = (
    #         f"| {{:<{name_width}}} | {{:<{student_code_width}}} "
    #         + " ".join([f"| {{:^5}} " for _ in other_headers])
    #         + "|"
    #     )

    #     line_length = (
    #         name_width
    #         + 2
    #         + student_code_width
    #         + 2
    #         + len(other_headers) * (other_width + 3 + 2)
    #         + 9
    #     )

    #     print("-" * line_length)
    #     print(row_format.format(name_header, student_code_header, *other_headers))
    #     print("-" * line_length)

    #     for obj in array_of_objects:
    #         values = [str(obj.__dict__.get(header, "")) for header in headers]
    #         name_value = values.pop(headers.index(name_header))
    #         student_code_value = values.pop(headers.index(student_code_header))
    #         print(row_format.format(name_value, student_code_value, *values))
    #         print("-" * line_length)
    # else:
    #     print("No data found in the CSV file.")


# def print_array_of_objects_of_a_record_in_table(array_of_objects):
#     student_code = input("Enter student code: ")
#     if array_of_objects:
#         headers = list(array_of_objects[0].__dict__.keys())
#         name_header = "Name"
#         student_code_header = "Student Code"
#         other_headers = [
#             header
#             for header in headers
#             if header not in [name_header, student_code_header]
#         ]

#         name_width = 30
#         student_code_width = 15
#         other_width = 3  # 1 space on each side + 3 for the value
#         row_format = (
#             f"| {{:<{name_width}}} | {{:<{student_code_width}}} "
#             + " ".join([f"| {{:^5}} " for _ in other_headers])
#             + "|"
#         )

#         line_length = (
#             name_width
#             + 2
#             + student_code_width
#             + 2
#             + len(other_headers) * (other_width + 3 + 2)
#             + 9
#         )

#         print("-" * line_length)
#         print(row_format.format(name_header, student_code_header, *other_headers))
#         print("-" * line_length)

#         for obj in array_of_objects:
#             if obj.__dict__.get(student_code_header) == f"BWU/BCA/23/{student_code}":
#                 values = [str(obj.__dict__.get(header, "")) for header in headers]
#                 name_value = values.pop(headers.index(name_header))
#                 student_code_value = values.pop(headers.index(student_code_header))
#                 print(row_format.format(name_value, student_code_value, *values))
#                 print("-" * line_length)
#     else:
#         print("No data found in the CSV file.")


# def print_no_student(array_of_objects):
#     print(f"Number of students without student code: {len(array_of_objects)}")


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
        number_of_assignments = int(input("Enter number of assignments submitted: "))
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


# def print_students_not_submitted_any(array_of_objects):
#     if array_of_objects:
#         headers = list(array_of_objects[0].__dict__.keys())
#         name_header = "Name"
#         student_code_header = "Student Code"
#         other_headers = [
#             header
#             for header in headers
#             if header not in [name_header, student_code_header]
#         ]

#         name_width = 30
#         student_code_width = 15
#         other_width = 3  # 1 space on each side + 3 for the value
#         row_format = (
#             f"| {{:<{name_width}}} | {{:<{student_code_width}}} "
#             + " ".join([f"| {{:^5}} " for _ in other_headers])
#             + "|"
#         )

#         line_length = (
#             name_width
#             + 2
#             + student_code_width
#             + 2
#             + len(other_headers) * (other_width + 3 + 2)
#             + 9
#         )

#         print("-" * line_length)
#         print(row_format.format(name_header, student_code_header, *other_headers))
#         print("-" * line_length)

#         for obj in array_of_objects:
#             if all(obj.__dict__.get(str(i), "") == "" for i in range(1, 8)):
#                 values = [str(obj.__dict__.get(header, "")) for header in headers]
#                 name_value = values.pop(headers.index(name_header))
#                 student_code_value = values.pop(headers.index(student_code_header))
#                 print(row_format.format(name_value, student_code_value, *values))
#                 print("-" * line_length)
#     else:
#         print("No data found in the CSV file.")

#     count = 0
#     for obj in array_of_objects:
#         if all(obj.__dict__.get(str(i), "") == "" for i in range(1, 8)):
#             count += 1
#             print(obj.__dict__["Student Code"], end=",")
#     print()
#     print(
#         f"Number of students who have not submitted any one of the assignments: {count}"
#     )


# def print_students_not_submitted_x(array_of_objects):
#     count = 0
#     while True:
#         x = int(input("Enter the number of assignment (1-7): "))
#         if 1 <= x <= 7:
#             break
#         else:
#             print("Invalid input. Please enter a number between 1 and 7.")
#     for obj in array_of_objects:
#         if obj.__dict__.get(str(x), "") != "Y":
#             count += 1
#     print(f"Number of students who have not submitted assignment no {x}: {count}")


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
            value_insert(array_of_objects, student_code, assignment_submission_array)
            update_file(file_path, array_of_objects)
        elif choice == 2:
            print_array_of_objects_in_table(array_of_objects)
        # elif choice == 3:
        #     print_array_of_objects_of_a_record_in_table(array_of_objects)
        # elif choice == 4:
        #     print_no_student(array_of_objects)
        # elif choice == 5:
        #     print_students_not_submitted_any(array_of_objects)
        # elif choice == 6:
        #     print_students_not_submitted_x(array_of_objects)
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")
