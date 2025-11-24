
#Task 1: Diary
import traceback

try:
   with open('diary.txt', 'a') as file:
      first_log = input("What happened today?")
      file.write(first_log  + "\n")
      subseq_log = input("What else?  (type done for now to quit)")
      while  subseq_log != "done for now":
         file.write(subseq_log  + "\n")
         subseq_log = input("What else?  (type done for now to quit)")

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
