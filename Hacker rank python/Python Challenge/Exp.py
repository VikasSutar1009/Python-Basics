from collections import defaultdict
employees = [
    {'id': 101, 'name': 'Sneha', 'department': 'IT', 'salary': 60000},
    {'id': 102, 'name': 'Ravi', 'department': 'HR', 'salary': 45000},
    {'id': 103, 'name': 'Amit', 'department': 'IT', 'salary': 52000},
    {'id': 104, 'name': 'Priya', 'department': 'Finance', 'salary': 48000},
    {'id': 105, 'name': 'Neha', 'department': 'IT', 'salary': 70000}
]

# print(employees)

# Print all employee names
# employees = ['Sneha', 'Ravi', 'Amit', 'Priya', 'Neha']
# for name in employees:
#     print(emp["name"])


# # Create a list of all employee salaries
# salaries = [emp["salary"] for emp in employees]
# print(salaries)

# # Find the total salary of all employees
# total_salary = sum(emp["salary"] for emp in employees)
# print(total_salary)

# # store all unique department name in a tuple
# departments = tuple(set(emp["department"] for emp in employees))
# print(departments)

# # Count how many employees work in the “IT” department.
# it_count = sum(1 for emp in employees if emp["department"] == "IT")
# print(it_count)

# # print names of employees earning more than 50,000
# for emp in employees:
#     if emp["salary"] > 50000:
#         print(emp["name"])

# # Find the length of the employee list
# length = len(employees)
# print("no of employeees:", length)

# # Reverse the order of employees in the list
# employees.reverse()
# print(employees)

# # Check if an employee named “Sneha” exists
# exists = any(emp["name"] == "Sneha" for emp in employees)
# print(exists)

# # Create a list of employee IDs only
# employee_id = [emp["id"] for emp in employees]
# print("List of employee id:",employee_id)

# # Find the employee with the highest salary
# highest_salary = max(employees, key = lambda emp: emp["salary"])
# print(highest_salary)

# Find the average salary of all employees
average_salary = sum(emp["salary"] for emp in employees) / len(employees)
print(average_salary)

# Display names of employees whose salary is below the average
for emp in employees:
    if emp["salary"] < average_salary:
        print(emp["name"])


# Sort employees by salary in descending order
sorted_employees = sorted(employees, key = lambda emp: emp["salary"], reverse=True)
for emp in sorted_employees:
    print(emp["name"], emp["salary"])

# Display all departments and total salary spent in each
dept_salary = defaultdict(int)
for emp in employees:
    dept_salary[emp["department"]] += emp["salary"]
    print(dict(dept_salary))

# Replace “IT” department name with “Technology” everywhere
for emp in employees:
    if emp["department"] == "IT":
        emp["department"] = "Technology"
        print(employees)

# Find all employees whose names start with ‘A’

a_names = [emp["name"] for emp in employees if emp["name"].startswith("A")]
print(a_names)

# Count total male and female employees
# gender_count = {"Male": 0, "Female": 0}
# for emp in employees:
#     gender_count[emp["gender"]] += 1

#     print(gender_count)

# 