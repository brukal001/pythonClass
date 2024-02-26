import random as rd
Given_money = 1000
win_score = 0
def roll_all_dice():
    dice_name = ["JHANDI","PURJA","ITTA","PAAN","HUKUM","CHIDI"]
    d1 = rd.choice(dice_name)
    d2 = rd.choice(dice_name)
    d3 = rd.choice(dice_name)
    d4 = rd.choice(dice_name)
    d5 = rd.choice(dice_name)
    d6 = rd.choice(dice_name)
    rolled_dice_set = [d1,d2,d3,d4,d5,d6]

    return rolled_dice_set

def get_choice():
   win_score = 0
   ch = input("""enter your choice in 
                                      Jhandi 
                                      Purja 
                                      Itta 
                                      Paan
                                      Hukum
                                      Chidi:
               """).upper()
   bet_price = int(input("Enter how much money Do you want to bet"))
   while True:
    global Given_money
    if bet_price > 0 and bet_price <= 1000:
     rolled_dice_set = roll_all_dice()
     if ch not in rolled_dice_set:
      Given_money = Given_money - bet_price
      print(f"YOu loose a bet so your money is {Given_money}")
     else:
       for i in rolled_dice_set:
         if ch == i:
           win_score += 1

    return win_score,bet_price
    
def bet_again():
  ag = input("Do you want to bet again Y/N").upper()
  if ag == "Y":
    main()
  else:
    print("coward")
def main():
   global Given_money 
   win_score,bet_price = get_choice()
   win_money = win_score * bet_price
   
   if win_score > 1:
     Given_money = Given_money + win_money
     print(f"your win and your money is {Given_money} ")
     bet_again()
   elif win_score == 1:
     print(f"Well say its a draw  and you have {Given_money}")
     bet_again()
   else:
     print(f"you loose {bet_price}")
     bet_again()
main()