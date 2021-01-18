#Joon Young Chang
#12-20-2020
# Python 3 program for Elo Rating 
import math 
import decimal

# Function to calculate the Probability 
def Probability(rating1, rating2): 
    ## 400 is universal number for elo rating system.
    ##This session is to process where the user belong.

    
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400)) 
  
def dropzeros(number):
    mynum = decimal.Decimal(number).normalize()
    # e.g 22000 --> Decimal('2.2E+4')
    return mynum.__trunc__() if not mynum % 1 else float(mynum)

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
        Ra = dropzeros(round(Ra + K * (1 - Pa))) 
        Rb = dropzeros(round(Rb + K * (0 - Pb))) 
      
  
    # Case -2 When Player B wins 
    # Updating the Elo Ratings 
    else : 
        Ra = dropzeros(round(Ra + K * (0 - Pa))) 
        Rb = dropzeros(round(Rb + K * (1 - Pb)))
      
  
    print("Updated Ratings:-")
    #round the answer to 0. 
    print("Ra =", round(Ra, 0)," Rb =", round(Rb, 0))
    ## This session is for player to get their rank tier and lp.
    if Ra in range (1000,1100):
        point = Ra - 1000
        print("Player A is Bronze 5",point, "lp")

    elif Ra in range (1100,1200):
        point = Ra - 1100
        print("Player A is Bronze 4",point, "lp")

    elif Ra in range (1200,1300):
        point = Ra - 1200
        print("Player A is Bronze 3",point, "lp")

    elif Ra in range (1300,1400):
        point = Ra - 1300
        print("Player A is Bronze 2",point, "lp")

    elif Ra in range (1400,1500):
        point = Ra - 1400
        print("Player A is Bronze 1",point, "lp")

    elif Ra in range (1500,1600):
        point = Ra - 1500
        print("Player A is Silver 5",point, "lp")

    elif Ra in range (1600,1700):
        point = Ra - 1600
        print("Player A is Silver 4",point, "lp")

    elif Ra in range (1700,1800):
        point = Ra - 1700
        print("Player A is Silver 3",point, "lp")

    elif Ra in range (1800,1900):
        point = Ra - 1800
        print("Player A is Silver 2",point, "lp")

    elif Ra in range (1900,2000):
        point = Ra - 1900
        print("Player A is Silver 1",point, "lp")

    elif Ra in range (2000,2100):
        point = Ra - 2000
        print("Player A is Gold 5",point, "lp")

    elif Ra in range (2100,2200):
        point = Ra - 2100
        print("Player A is Gold 4",point, "lp")

    elif Ra in range (2200,2300):
        point = Ra - 2200
        print("Player A is Gold 3",point, "lp")

    elif Ra in range (2300,2400):
        point = Ra - 2300
        print("Player A is Gold 2",point, "lp")

    elif Ra in range (2400,2500):
        point = Ra - 2400
        print("Player A is Gold 1",point, "lp")

    elif Ra in range (2500,2600):
        point = Ra - 2500
        print("Player A is Platinum 5",point, "lp")

    elif Ra in range (2600,2700):
        point = Ra - 2600
        print("Player A is Platinum 4",point, "lp")

    elif Ra in range (2700,2800):
        point = Ra - 2700
        print("Player A is Platinum 3",point, "lp")

    elif Ra in range (2800,2900):
        point = Ra - 2800
        print("Player A is Platinum 2",point, "lp")

    elif Ra in range (2900,3000):
        point = Ra - 2900
        print("Player A is Platinum 1",point, "lp")

    elif Ra in range (3000,3100):
        point = Ra - 3000
        print("Player A is Diamond 5",point, "lp")

    elif Ra in range (3100,3200):
        point = Ra - 3100
        print("Player A is Diamond 4",point, "lp")

    elif Ra in range (3200,3300):
        point = Ra - 3200
        print("Player A is Diamond 3",point, "lp")

    elif Ra in range (3300,3400):
        point = Ra - 3300
        print("Player A is Diamond 2",point, "lp")

    elif Ra in range (3400,3500):
        point = Ra - 3400
        print("Player A is Diamond 1",point, "lp")

    elif Ra >= 3500:
        point = Ra - 3500
        print ("Player A is Challenger",point, "lp")

    elif Ra <= 1000:
        point = Ra - 1000
        print ("Player A is Iron")
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
