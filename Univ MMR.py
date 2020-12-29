#Joon Young Chang
#12-20-2020
# Python 3 program for Elo Rating 
import math 
  
# Function to calculate the Probability 
def Probability(rating1, rating2): 
    ## 400 is universal number for elo rating system.
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400)) 
  
  
# Function to calculate Elo rating 
# K is a constant. 
# d determines whether 
# Player A wins or Player B.  
def EloRating(Ra, Rb, K, d): 
   
  
    # To calculate the Winning 
    # Probability of Player B 
    Pb = Probability(Ra, Rb) 
  
    # To calculate the Winning 
    # Probability of Player A 
    Pa = Probability(Rb, Ra) 
  
    # Case -1 When Player A wins 
    # Updating the Elo Ratings 
    if (d == 1) : 
        Ra = Ra + K * (1 - Pa) 
        Rb = Rb + K * (0 - Pb) 
      
  
    # Case -2 When Player B wins 
    # Updating the Elo Ratings 
    else : 
        Ra = Ra + K * (0 - Pa) 
        Rb = Rb + K * (1 - Pb) 
      
  
    print("Updated Ratings:-")
    #round the answer to 0. 
    print("Ra =", round(Ra, 0)," Rb =", round(Rb, 0)) 
  
# Driver code 
  
# Ra and Rb are current ELO ratings 
Ra = input("Enter MMR for Player A: ")
Ra=int(Ra)
Rb = input("Enter MMR for Player B: ")
Rb=int(Rb)
##if K gets bigger, it will make effect on MMR bigger.
#K is developers rating, if the player played more than hundreds of game than the k will be close to 20
# if player played less than 100s and have winning streak, k will be 40-50
#K = input("this number will be developer's number where you can control between 20-50: ")
K = input("Consecutive wins from this player? if it is winning streak, type number, if losing streak, type -number: " )
K = int(K)
## please look over readme for more explanation.
if K in range (-100,-20):
    K = 10
elif K in range (-20,-10):
    K = 15
elif K in range (-10,-5):
    K = 20
elif K in range (-5,-3):
    K = 25
elif K in range (-5,0):
    K = 35
elif K in range (0,2):
    K = 30
elif K in range (2,4):
    K = 40
elif K in range (4,6):
    K = 45
elif K in range (6,10):
    K = 50
else: 
    K = 60
d = input("if win = 1, else = other number: ")
d = int(d)
EloRating(Ra, Rb, K, d) 
  
# This code is contributed by 
# Smitha Dinesh Semwal and modified by Joon Young Chang
