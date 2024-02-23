''' Given an array of integer find the count of odd and even digits'''

'''
def find_odd_even_count(arr):
    
    counter = {
            "odd" : 0,
            "even": 0
        }
   
    for i in arr:
        if arr[i] % 2 == 0:
            counter["even"]= counter["even"] + 1

        else:
            counter["odd"]= counter["odd"] + 1


        print(counter)
        
arr = [1 , 2, 3, 4, 5, 6, 7, 8 ,9]
find_odd_even_count(arr)'''


def factorial(n):
    f = 1
    for i in range(1, n+1):
      f = f * i
    return f

n = int(input("enter a number: "))
result = factorial(n)
print(result)
