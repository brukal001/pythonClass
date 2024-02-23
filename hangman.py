
import random as rd
print(""" 
------------------- Word Guessing Game ---------------
             ---------HangMan------------
      You will have 5 chance to guess the word
              Welcome to the Game
""")

word = ["knife","computer","world","copy"]
rand_word = rd.choice(word)
# len = len(rand_word)
upr = rand_word.upper()
display = []
for i in rand_word:
    display += "_"
print(display)

def check(lives=5):
    while lives != 0:
      if display == [*upr]:
        print("""----------YOU WIN----------
              AND YOU GOT BLESSING FORM GOD
              ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ
              """)
        exit()
      while display != [*upr]:
       ask = input("enter any letter:  ").upper()
       print(ask)
       for i in upr:
         if ask == i:
            index = upr.index(ask)
            display[index] = ask
            print(display)
            check()
            break 
       for i in upr:
        if ask != i: 
          lives -= 1
          print(f"you have only {lives} left")
          break
        else:
           check(lives)
       if lives == 0:
           print("--------You Loose---------")
           print("""-------------Thank You For Playing----------
                    -------------AArigato Gojai Maas---------
                 """)
           break
       
     


        

check() 