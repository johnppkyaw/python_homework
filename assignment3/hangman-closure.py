#Task 4: Closure Practice

def make_hangman(secret_word):
  guesses = []
  def hangman_closure(letter):
    guesses.append(letter)
    solution = ""
    for letter in secret_word:
      if(letter in guesses):
        solution += letter
      else:
        solution += "_"
    print(solution)
    if "_" in solution:
      return False
    else:
      return True
  return hangman_closure

hangman_game = make_hangman(input("Enter a secret word: "))
letter_input = input("Guess another letter: ")
while(hangman_game(letter_input) == False):
  letter_input = input("Guess another letter: ")
  
