import random

print("You will get 5 attempts to guess a correct number.")
print("Guess any number between 1 and 10")
i = 0
a = random.randint( 1 , 10 )

while(i<5):
  print("Guess a number...")
  n = input("type any number: ")
  if int(n) == (a):
    print("Ding Ding Ding, you got it right!")
    i=5
  elif int(n) > (a):
    print(" You guess too high")
  else:
    print(" You guess too low")
  i = i+1  
