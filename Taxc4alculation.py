'''Wap to accept then cost price of a bike and display the road tax to be paid according to the following criterias
Cost price (in Rs)      Tax
>100000             15%
>50000 and <=100000    10%
<= 50000             5%
  '''
t = (0.15,0.10,0.5)
Cp = int(input("enter cost price of the bike: "))
if Cp >100000:
    print(f" Road tax to be paid is Rs {t[0]*Cp}")

elif   Cp >50000 and Cp <=100000:
    print(f"Road tax to be paid is Rs {t[1]*Cp}")

elif   Cp <=50000:
    print(f"Road tax to be paid is Rs {t[2]*Cp} ")   
   