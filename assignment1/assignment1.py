#Task 1: Hello
def hello():
  return "Hello!"

#Task 2: Greet with a Formatted String
def greet(name):
  return "Hello, " + name + "!"

#Task 3: Calculator
def calc(arg1, arg2, arg3="multiply"):
  try:
    match arg3:
      case "add":
        return arg1 + arg2
      case "subtract":
        return arg1 - arg2
      case "divide":
        return arg1 / arg2
      case "modulo":
        return arg1 % arg2
      case "int_divide":
        return arg1 // arg2
      case "power":
        return arg1 ** arg2
      case _:
        return arg1 * arg2
  except TypeError:
    return "You can't " + arg3 + " those values!"
  except ZeroDivisionError:
    return "You can't divide by 0!"

#Task 4: Data Type Conversion
def data_type_conversion(value, name):
  try:
    match name:
      case "int":
        return int(value)
      case "float":
        return float(value)
      case _:
        return str(value)
    return 
  except ValueError:
    return f"You can't convert {value} into a {name}."

#Task 5: Grading System, Using *args
def grade(*args):
  try:
    average = sum(args) / len(args)
    if average >= 90:
      return 'A'
    elif average >= 80:
      return 'B'
    elif average >= 70:
      return 'C'
    elif average >= 60:
      return 'D'
    else:
      return 'F'
  except TypeError:
    return "Invalid data was provided."

#Task 6: Use a For Loop with a Range
def repeat(string, count):
  result = ""
  for i in range(count):
    result += string
  return result

#Task 7: Student Scores, Using **kwargs
def student_scores(position, **kwargs):
  num_student = len(kwargs.items())
  total_score = 0
  current_max_score = 0
  best_student = ""
  for key, value in kwargs.items():
      total_score += value
      if (value > current_max_score):
        current_max_score = value
        best_student = key
  if position == "best":
    return best_student
  else:
    return total_score / num_student
  
#Task 8: Titleize, with String and List Operations
def titleize(string):
  words = string.split()
  little_words = ['a', 'on', 'an', 'the', 'of', 'and', 'is', 'in']
  words[0] = words[0].capitalize()
  words[-1] = words[-1].capitalize()
  for i, word in enumerate(words):
    if word in little_words or i == 0 or i == len(words) :
        continue
    words[i] = word.capitalize()
  return " ".join(words)

#Task 9: Hangman, with more String Operations
def hangman(secret, guess):
  result = ""
  for letter in secret:
    if(letter in guess):
      result += letter
    else:
      result += "_"
  return result

#Task 10: Pig Latin, Another String Manipulation Exercise
  #eat => eatay
  #phone => onephay
  #quota => otaquay
def pig_latin(string):
  result_words = []
  words = string.split()
  for word in words:
    pig_latin_word = ''
    if word[0] in 'aeiou':
      pig_latin_word += word
      pig_latin_word += "ay"
      result_words.append(pig_latin_word)
    else:
      consonant_string = ""
      stop_index = 0
      for letter in word:
        if letter in 'aeio':
          break
        consonant_string += letter
        stop_index += 1
      pig_latin_word += word[stop_index:len(word)]
      pig_latin_word += consonant_string
      pig_latin_word += "ay"
      result_words.append(pig_latin_word)
  return " ".join(result_words)
