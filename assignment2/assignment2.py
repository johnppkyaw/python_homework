import csv
import traceback
import os
import custom_module
from datetime import datetime

#Task 2: Read a CSV File
def read_employees():
  fields_dict = {}
  rows_list = []
  try:
    with open('../csv/employees.csv', 'r') as file:
      reader = csv.reader(file)
      for row_index, row in enumerate(reader):
        if(row_index == 0):
          fields_dict['fields'] = row
        else:
          rows_list.append(row)
      fields_dict['rows'] = rows_list
    return fields_dict
  except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
      print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")

employees = read_employees()

#Task 3: Find the Column Index
def column_index(string):
  return employees["fields"].index(string)

employee_id_column = column_index("employee_id")

#Task 4: Find the Employee First Name
def first_name(requested_row):
  first_name_column = column_index("first_name")
  return employees["rows"][requested_row][first_name_column]

#Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
  def employee_match(row):
   return int(row[employee_id_column]) == employee_id
  matches=list(filter(employee_match, employees["rows"]))
  return matches
  
#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
  matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
  return matches

#Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
  last_name_column = column_index("last_name")
  employees["rows"].sort(key=lambda row : row[last_name_column])
  return employees["rows"]

print(sort_by_last_name())

#Task 8: Create a dict for an Employee
def employee_dict(row):
  result_dict={}
  for field in employees['fields']:
    if field != 'employee_id':
      result_dict[field] = row[column_index(field)]
  return result_dict

print(employee_dict(employees["rows"][0]))

#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
  all_employees = {}
  for employee in employees['rows']:
    all_employees[employee[0]] = employee_dict(employee)
  return all_employees

#Task 10: Use the os Module
def get_this_value():
  return os.getenv('THISVALUE')

#Task 11: Creating Your Own Module
def set_that_secret(new_secret):
  custom_module.set_secret(new_secret)

set_that_secret('John was here')
print(custom_module.secret)

#Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
  minutes1 = {}
  minutes2 = {}
  def create_minutes(filename, dict):
    rows = []
    try:
      with open(filename, 'r') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
          if(index == 0):
            dict['fields'] = row
          else:
            rows.append(tuple(row))
      dict['rows'] = rows
    except Exception as e:
      trace_back = traceback.extract_tb(e.__traceback__)
      stack_trace = list()
      for trace in trace_back:
          stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
      print(f"Exception type: {type(e).__name__}")
      message = str(e)
      if message:
          print(f"Exception message: {message}")
      print(f"Stack trace: {stack_trace}")
  create_minutes('../csv/minutes1.csv', minutes1)
  create_minutes('../csv/minutes2.csv', minutes2)
  return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

#Task 13: Create minutes_set
def create_minutes_set():
  set1 = set(minutes1['rows'])
  set2 = set(minutes2['rows'])
  union_set = set1.union(set2)
  return union_set

minutes_set = create_minutes_set()

#Task 14: Convert to datetime
def create_minutes_list():
  minutes_list = list(minutes_set)
  converted_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
  return converted_list

minutes_list = create_minutes_list()
print(minutes_list)

#Task 15: Write Out Sorted List
def write_sorted_list():
  minutes_list.sort(key=lambda row : row[1])
  converted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
  try:
    with open('minutes.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(minutes1['fields'])
      for eachRow in converted_list:
        writer.writerow(eachRow)
  except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
      print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
  return converted_list

write_sorted_list()
