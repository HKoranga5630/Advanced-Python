# Dynamic Report Generator using Decorators, Class Methods,
# and Magic Methods

# Decorator to add a title to a report
def add_title(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        return f"========== {self.title} ==========\n{result}"
    return wrapper


class Report:
    # Class variable
    report_count = 0

    def __init__(self, title, data, template="default"):
        self.title = title
        self.data = data
        self.template = template
        Report.report_count += 1

    # Class method to create a report from a dictionary
    @classmethod
    def create_report(cls, title, data, template="default"):
        return cls(title, data, template)

    # Decorator applied to the report generation method
    @add_title
    def generate_report(self):
        if self.template == "table":
            return self.format_table()
        elif self.template == "list":
            return self.format_list()
        else:
            return self.format_default()

    # Default formatting
    def format_default(self):
        output = ""
        for key, value in self.data.items():
            output += f"{key}: {value}\n"
        return output.strip()

    # Table formatting
    def format_table(self):
        output = f"{'Field':<20} | {'Value':<20}\n"
        output += "-" * 43 + "\n"

        for key, value in self.data.items():
            output += f"{key:<20} | {str(value):<20}\n"

        return output.strip()

    # List formatting
    def format_list(self):
        output = ""
        for key, value in self.data.items():
            output += f"- {key}: {value}\n"
        return output.strip()

    # Magic method to define how the object is printed
    def __str__(self):
        return self.generate_report()

    # Magic method to return the number of fields in the report
    def __len__(self):
        return len(self.data)

    # Magic method to support the + operator
    def __add__(self, other):
        combined_data = self.data.copy()
        combined_data.update(other.data)

        return Report(
            title=f"{self.title} + {other.title}",
            data=combined_data,
            template=self.template
        )


# Main Program
if __name__ == "__main__":

    # Report data
    student_data = {
        "Student Name": "Rahul",
        "Roll Number": 101,
        "Course": "B.Tech CSE",
        "Marks": 85
    }

    # Create a report using the class method
    report1 = Report.create_report(
        "Student Report",
        student_data,
        template="table"
    )

    # Display the report
    print(report1)

    # Display the number of fields
    print("\nNumber of fields:", len(report1))

    # Create another report
    attendance_data = {
        "Attendance": "92%",
        "Semester": 3
    }

    report2 = Report.create_report(
        "Attendance Report",
        attendance_data,
        template="list"
    )

    print("\n" + str(report2))

    # Combine two reports using the + operator
    combined_report = report1 + report2

    print("\nCombined Report:")
    print(combined_report)

    # Display total reports created
    print("\nTotal reports created:", Report.report_count)