hangman_lives_dict = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }
import random as rd
print(""" 
------------------- Word Guessing Game ---------------
             ---------HangMan------------
      You will have 5 chance to guess the word
              Welcome to the Game
""")

word = ["knife","computer","world","copy","night","stage","china","cow","gun","hospital"]
rand_word = rd.choice(word)
len = len(rand_word)
upr = rand_word.upper()
display = []
for i in rand_word:
    display += "_"
print(display)

def check(lives=7):
    while lives != 0:
      if display == [*upr]:
        print("""----------YOU WIN----------
              AND YOU GOT BLESSING FORM GOD
              ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ ॐ 
              """)
        exit()
      while display != [*upr]:
       ask = input("enter any letter:  ").upper()
       print(ask)
      #  hint(upr,display,lives)
       for i in upr:
         if ask == i:
            index = upr.index(ask)
            display[index] = ask
            print(display)
            check(lives)
            break 
       for i in upr:
        if ask != i: 
          lives -= 1
          stages(lives)    
          print(f"you have only {lives} left")
          break
        else:
           check(lives)
 
       
     

def stages(lives):
  if lives == 7:
    print(hangman_lives_dict[lives])
    print(display)
  elif lives == 6:
    print(hangman_lives_dict[lives])
    print(display)
  elif lives == 5:
    print(hangman_lives_dict[lives])
    print(display)
  elif lives == 4:
    print(hangman_lives_dict[lives])
    print(display)
  elif lives == 3:
    print(hangman_lives_dict[lives])
    print(display)
  elif lives == 2:
    print(hangman_lives_dict[lives])
    print(display)
  elif lives == 1:
    print(hangman_lives_dict[lives])
    print(display)
  else:
    if lives == 0:
           print(hangman_lives_dict[lives])
           print("--------You Loose---------")
           print("""-------------Thank You For Playing----------
                    -------------AArigato Gojai Maas---------
                 """)
           exit()
    
# def hint(upr,display,lives):
#  c = [*upr]
# #  for j in range(3):
#  while  lives < 4 :
#     get_hint = input("if you want hint type h for hint n for skip the option:  ").upper()
#     if get_hint == "H":
#        for i in range(len):
#          while c[i] not in display:
#             print(c[i])
#             break  
#          break  

       
       
    # else:
    #  check(lives)

  

   
        

check() 