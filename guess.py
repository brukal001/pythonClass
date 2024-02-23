import random

def main():
    print("=== Number Guesing Game: ")

    Computer_number = random.randint(1,10)
    DIFFERENCE_THRESHOLD = 5

    while True:
      try:
        user_guess = int(input("Enter your guess: "))
      except Exception:
        print("please enter a valid number")
        continue
      
      if user_guess == Computer_number:
         print("You Win!!")
         break
      elif user_guess > Computer_number:
         difference = user_guess - Computer_number
         if difference > DIFFERENCE_THRESHOLD:
            print("Too High")
         else:
            print("High")
      else:
         difference = Computer_number - user_guess
         if difference > DIFFERENCE_THRESHOLD:
            print("Too low")
         else:
            print("low")
main()            