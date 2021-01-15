# Project Name
# MMR-system-for-IE
This MMR system is made for Isekai Eternal.
# <a name="team-members"></a>Team Members
* "Joon Young Chang" <joonyoung@andrews.edu>
# detail description
According to this system, we could put base MMR as 1000.
from 1000, we could make system like
1000-1100 bronze 5
1100-1200 bronze 4
1200-1300 bronze 3
1300-1400 bronze 2
1400-1500 bronze 1
1500-1600 silver 5
1600-1700 silver 4
1700-1800 silver 3
1800-1900 silver 2
1900-2000 silver 1
2000-2100 Gold 5 
2100-2200 Gold 4
2200-2300 Gold 3
2300-2400 Gold 2
2400-2500 Gold 1
2500-2600 platinum 5
2600-2700 platinum 4
2700-2800 platinum 3
2800-2900 platinum 2
2900-3000 platinum 1
3000-3100 Diamond 5
3100-3200 Diamond 4
3200-3300 Diamond 3
3300-3400 Diamond 2
3400-3500 Diamond 1
3500-     Challenger

After 3500, challenger will be challenger but it will have point system keep going up only.
Users will only see last two digit of the MMR (ex. 1345 === bronze 2 45p)


Take a close look on developer's number K
This number specifically controls number of the points that the player will get.
# As you take a close look, you will realize that when they clear out the losing streak, they will have equal chance with others.
# This system will make sure as long as they try, they will get to as much tier as they want.
# Instead of "Cushion", losers will lose less points as they kept on losing, winners will take normal points.
if K in range (-100,-20):
    K = 10
elif K in range (-20,-10):
    K = 15
elif K in range (-10,-5):
    K = 20
elif K in range (-5,-3):
    K = 25
elif K in range (-5,0):
    K = 30
elif K in range (0,2):
    K = 35
elif K in range (2,4):
    K = 40
elif K in range (4,6):
    K = 45
elif K in range (6,10):
    K = 50
else: 
    K = 60



    In case of JunHyeong's play,
    he lost first game so from 1000, he lost 15 points.
    then he won a game, he gained 18 points
    then he won again, he gained 15 points
    so he has 1018 MMR currently.



    안녕하세요!