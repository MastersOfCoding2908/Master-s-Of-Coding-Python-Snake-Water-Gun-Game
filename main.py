# Channnel Name - Master's Of Coding

# Snake, Water, Gun Game In Python.
################################################################
# Importing Random Module

import random
################################################################
# All Variables

s_w_g = ["Snake", "Water", "Gun"]
computer = random.choice(s_w_g)
Player_Name = input("What's Your Name ? :")
################################################################
# Print Statement

print("Snake , Water And Gun Game.")
print(f"Hello, {Player_Name.upper()}")
################################################################
# Print Statement And Input Statement

user = input('''For Snake Press 's' , For Water Press 'w' And For Gun Press 'g' 
User Choose : ''')
user = user.lower()
print(f"Computer Choose : {computer}")
################################################################
# Check User Input Whether It Is Correct Or Incorrect

if user =='s' or user == 'w':
    pass
elif user == 'g':
    pass
else:
    print('You Have Entered A Invalid Input.')
    print('Please Try Again !')
    exit()
################################################################
# Main Logic Using If Then Else Ladder...

if user == "s" and computer == "Snake":
   print("\nGame Tie !")
   print("Try Again!\n")
elif user == "s" and computer == "Water":
   print("\nCongratulations ! You Won.")
   print("Play Again!\n")
elif user == "s" and computer == "Gun":
   print("\nYou Lost!")
   print("Try Again!\n")
################################################################

elif user == "w" and computer == "Water":
   print("\nGame Tie !")
   print("Try Again!\n")
elif user == "w" and computer == "Snake":
    print("\nYou Lost!")
    print("Try Again!\n")
elif user == "w" and computer == "Gun":
    print("\nCongratulations ! You Won.")
    print("Play Again!\n")
################################################################

elif user == "g" and computer == "Gun":
    print("\nGame Tie !")
    print("Try Again!\n")
elif user == "g" and computer == "Snake":
    print("\nCongratulations ! You Won.")
    print("Play Again!\n")
elif user == "g" and computer == "Water":
    print("\nYou Lost!")
    print("Try Again!\n")
################################################################

else:
     pass
################################################################
# If Then Else Ladder End...
################################################################
# Print Statement

print(f"\t\tThank You For Playing This Game ! {Player_Name.upper()}")
################################################################
################################################################

# @MastersOfCoding2908
# Please Like, Share, Comment And Subscribe My Channel To Get More Content Releated to Programming.
# My Channel Link  - https://www.youtube.com/@MastersOfCoding2908
# Source Code And Its Full Explanation Is Given In The Description And Pinned In The Comment Box.