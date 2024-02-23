import random
def playAgain():
  i = input("If you want to continue Y/N:  ")
  while i is not None:
    if i.upper() == "Y":
     main()
    else:
     print("------- Thank You for Playing -------")
     break
  
def main():
  ch = ["ROCK", "PAPER", "SCISSOR"]
  computer_choose = random.choices(ch)
  a  = input("----------Chosse Rock, Paper or Scissor -----------\n  ")
  user_choose = a.upper()
  count = {
    "User_wins":0,
    "Computer_wins":0
  }

  while True:
    if user_choose == computer_choose:
      print("--------TIE---------")
      count["Computer_wins"] += 1
      count["User_wins"] +=1
      print(f"---------Computer Choice : {computer_choose}--------")
      print(f"---------YOur Choice :['{user_choose}']--------")
      print(count)
      playAgain()
       
    elif user_choose == "ROCK" and computer_choose == "PAPER":
      print("------------ YOU LOOSE ----------")
      count["Computer_wins"] += 1
      print(f"---------Computer Choice : {computer_choose}--------")
      print(f"---------YOur Choice : ['{user_choose}']--------")
      print(count)
      playAgain()
     
    elif user_choose == "ROCK" and computer_choose == "SCISSOR":
      print("----------YOU WIN---------")
      count["User_wins"] +=1
      print(f"---------Computer Choice : {computer_choose}--------")
      print(f"---------YOur Choice : ['{user_choose}']--------")
      print(count)
      playAgain()
      
    elif user_choose == "PAPER" and computer_choose == "ROCK":
      print("-------YOU WIN------")
      count["User_wins"] +=1
      print(f"---------Computer Choice : {computer_choose}--------")
      print(f"---------YOur Choice : ['{user_choose}']--------")
      print(count)
      playAgain()
    elif user_choose == "PAPER" and computer_choose == "SCISSOR":
      print("-------YOU LOOSE---------")
      count["Computer_wins"] += 1
      print(f"---------Computer Choice : {computer_choose}--------")
      print(f"---------YOur Choice : ['{user_choose}']--------")
      print(count)
      playAgain()
    elif user_choose == "SCISSOR" and computer_choose == "PAPER":
      print("--------- YOU WIn ---------")
      count["User_wins"] +=1
      print(f"---------Computer Choice : {computer_choose}--------")
      print(f"---------YOur Choice : ['{user_choose}']--------")
      print(count)
      playAgain()
    else:
      print("------- YOU LOOSE ---------")
      count["Computer_wins"] += 1
      print(f"---------Computer Choice : {computer_choose}--------")
      print(f"---------YOur Choice : ['{user_choose}']--------")
      print(count)
      playAgain()
    

main()