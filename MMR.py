##Joon Young Chang
##12-14-2020
## Basic coding for MMR system based on elo calculator

ratA = input("Enter MMR for Player A: ")
ratB = input("Enter MMR for Player B: ")
print(ratA, ratB)
ratA=int(ratA)
ratB=int(ratB)
#wp is winning point, depending on the winning ratio of A and B, this number will change.
#if wp = 800 then A has 100 times more possiblity to win.
#As wp gets bigger and bigger, it will adjust the number of winner's mmr or loser's mmr within the range of dev
wpA = input("win ratio of A: ")
wpB = input("win ratio of B: ")
wpA = int(wpA)
wpB = int(wpB)
wp = (.5+wpA-wpB)*10
rat =  (100+ ratA - ratB)/ wp
## this will generate the number ratio for mmr
expected = 1 /(10**rat)

## adding to elo rating formula

## 20 is developer rating
#by changing dev, this will change MMR drastically
#as winning streak gets bigger and bigger, dev number will change up to 40
#as losing streak gets bigger, dev number will be lower than 20
dev = 20
score_change = dev * (1 - expected)

## adding up depends on win or lose

match = input("type win if A won the match: ")

if match == 'win' :
    ratA = ratA + score_change
    ratB = ratB - score_change
else:
    ratA = ratA - score_change
    ratB = ratB + score_change

print("MMR for A",ratA,"MMR for B",ratB)

