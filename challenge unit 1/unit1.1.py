#1.1 implement a recursive function to calculate the factortal of a given number 
def recur_factortal(n):
  if n ==1:
    return n
  else:
    return n*recur_factortal(n-1)
    #take input from the user
num=int(input("enter a number:"))
#check is the number is negative
if num<0:
  print("sorry,factortal dose not exist for negative numbers")
elif num==0:
  print("the factotal of 0 is 1")
else:
  print("the factortal of",num,"is",recur_factortal(num))

