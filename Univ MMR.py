#Joon Young Chang
#12-20-2020
# Python 3 program for Elo Rating 
import math 
  
# Function to calculate the Probability 
def Probability(rating1, rating2): 
  
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
    print("Ra =", round(Ra, 6)," Rb =", round(Rb, 6)) 
  
# Driver code 
  
# Ra and Rb are current ELO ratings 
Ra = input("Enter MMR for Player A: ")
Ra=int(Ra)
Rb = input("Enter MMR for Player A: ")
Rb=int(Rb)
##if K gets bigger, it will make effect on MMR bigger.
K = input("this number will be developer's number where you can control between 20-50: ")
K = int(K)
d = input("if win = 1, else = other number: ")
d = int(d)
EloRating(Ra, Rb, K, d) 
  
# This code is contributed by 
# Smitha Dinesh Semwal and modified by Joon Young Chang
