# ===============================
# Student Academic Performance System
# Google Colab Version
# ===============================

# Fixed department info (tuple)
department_info = ("Religion Department", "Faculty of Technology", 2025)

# Unique courses (set)
unique_courses = {"Python", "Statistics", "Data Science", "Algorithms"}

# Student data (list of dictionaries)
students = [
    {
        "name": "Rasheed Fatia",
        "matric": "23/60AC389",
        "age": 22,
        "cgpa": 4.81,
        "is_active": True,
        "courses": ["Python", "Statistics", "Data Science"],
        "outstanding_courses": 0
    },
    {
        "name": "Yusuf Adeoye",
        "matric": "23/70JC093",
        "age": 23,
        "cgpa": 3.45,
        "is_active": True,
        "courses": ["Python", "Statistics"],
        "outstanding_courses": 0
    },
    {
        "name": "Moses Oyedele",
        "matric": "23/22KY120",
        "age": 24,
        "cgpa": 2.40,
        "is_active": True,
        "courses": ["Algorithms", "Data Science"],
        "outstanding_courses": 1
    },
    {
        "name": "Timi Abidoye",
        "matric": "23/10AB501",
        "age": 21,
        "cgpa": 4.12,
        "is_active": True,
        "courses": ["Python", "Electronics"],
        "outstanding_courses": 0
    },
    {
        "name": "Nimah Nina",
        "matric": "23/90NN999",
        "age": 20,
        "cgpa": 4.02,
        "is_active": False,
        "courses": ["Statistics", "Data Science"],
        "outstanding_courses": 0
    }
]

print("Student records loaded successfully.")
print("Total students:", len(students))

import ipywidgets as widgets
from IPython.display import display, clear_output

def view_students(btn):
    clear_output()
    print("LIST OF STUDENTS")
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']} - CGPA: {s['cgpa']}")

def top_performer(btn):
    clear_output()
    top = max(students, key=lambda x: x["cgpa"])
    print("TOP PERFORMER")
    print("Name:", top["name"])
    print("Matric:", top["matric"])
    print("CGPA:", top["cgpa"])
    print("Courses:", top["courses"])

def eligibility_check(btn):
    clear_output()
    name = name_input.value
    for s in students:
        if s["name"].lower() == name.lower():
            eligible = (
                s["cgpa"] >= 2.5 and
                s["outstanding_courses"] == 0 and
                s["is_active"]
            )
            print("Eligibility Check Result")
            print("Name:", s["name"])
            print("CGPA:", s["cgpa"])
            print("Outstanding Courses:", s["outstanding_courses"])
            print("Active:", s["is_active"])
            print("Eligible:", eligible)
            return
    print("Student not found.")

# Widgets
btn_view = widgets.Button(description="View All Students")
btn_top = widgets.Button(description="Find Top Performer")
btn_eligibility = widgets.Button(description="Check Graduation Eligibility")
name_input = widgets.Text(description="Student Name:")

btn_view.on_click(view_students)
btn_top.on_click(top_performer)
btn_eligibility.on_click(eligibility_check)

display(btn_view, btn_top, name_input, btn_eligibility)

