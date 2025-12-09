#Task 3: List Comprehensions Practice
import csv
import traceback

try:
  with open('../csv/employees.csv', 'r') as file:
    reader = csv.reader(file)
    employee_names = [f"{row[1]} {row[2]}" for row_index, row in enumerate(reader) if row_index != 0]
    print(employee_names)
    
    emp_names_with_e = [name for name in employee_names if "e" in name]
    print(emp_names_with_e)

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
