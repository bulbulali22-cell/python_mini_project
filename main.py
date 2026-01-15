#  we all have played snake,water gun game in out childhood.if you havent google the rules of this game and write a python program capable of playing this game with the user
import  random
computer = random.choice([-1,0,1])
youstr = input("enter your choice:")
youDict = {"s" : 1, "w" : -1, "g" : 0 }
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = youDict[youstr]

#  me and my computer choose two numbers

print(f"you choose{reverseDict[you]}\n computer choose{reverseDict[computer]}")

if(computer == you):
    print("Its a draw")


else:
    if((computer - you ) == -1 or (computer - you) == 2):
      print("Ypu lose")

    else:
      print("You Win")





    