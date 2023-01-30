import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game = [rock,paper,scissors]
randnum= random.randint(0,len(game)-1)
comp = game[randnum]
user =input("Choose your pick: R for Rock, P for Paper, S for Scissors\n")
if user == "R":
  print("You played with\n")
  print(rock) 
  if comp ==rock:
    print("Comp played with\n"+rock)
    print("It's a tie")
  elif comp ==paper:
    print("Comp played with\n"+paper)
    print("Comp wins.")
  else:
    print("Comp played with\n"+scissors)
    print("You won!") 
if user == "P":
  print("You played with\n")
  print(paper)
  if comp ==rock:
    print("Comp played with\n"+rock)
    print("You won!")
  elif comp ==paper:
    print("Comp played with\n"+paper)
    print("It's a tie")
  else:
    print("Comp played with\n"+scissors)
    print("You lost!")
if user =="S":
  print("You played with\n")
  print(scissors)
  if comp ==rock:
    print("Comp played with\n"+rock)
    print("You lost!")
  elif comp ==paper:
    print("Comp played with\n"+paper)
    print("You won!")
  else:
    print("Comp played with\n"+scissors)
    print("It's a tie!")

  
 
    
