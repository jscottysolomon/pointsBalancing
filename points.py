import math
from sympy import *

# Event Variables
teamSize = 4
teamCount = 8
N = teamSize * teamCount
TOTAL = 5500
print("Team size: ", teamSize)
print("Team count: ", teamCount)
print("Number of Players: ", N)
print("------------------------")

# Math Variables
x = symbols('x')
y = symbols('y')

# Survival Games
def survivalGames(WP):
    AAE = 2 # Alive At End
    kills = N - AAE

    a = integrate(y*x, (x,AAE,N))
    equation = Eq(a+(10*kills*y)+WP, TOTAL)

    solution = solve(equation, y)
    decimal_solution = [float(sol.evalf()) for sol in solution]
    survivalPoints = round(decimal_solution[0] * 2) / 2
    killPoints = survivalPoints * 10
    
    print("Survival Games")
    print("\tWin Points:", WP)
    print("\tSurvival Points: ", survivalPoints)
    print("\tKill Points: ", killPoints)

# Bingo
def bingo():
    itemNumber = 24

    fourFinishes = 14
    threeFinishes = 3
    twoFinishes = 1
    oneFinish = 4

    multiplier = 0.2

    a = integrate(y-(y*multiplier*x), (x,0,4))
    b = integrate(y-(y*multiplier*x), (x,0,3))
    c = integrate(y-(y*multiplier*x), (x,0,2))
    d = integrate(y-(y*multiplier*x), (x,0,1))

    equation = Eq(fourFinishes*a+threeFinishes*b+twoFinishes*c+oneFinish*d, TOTAL)
    solution = solve(equation, y)

    decimal_solution = [float(sol.evalf()) for sol in solution]

    initial = round(decimal_solution[0])
    drop = round(initial * 0.2 * 2) / 2

    print("Bingo")
    print("\tInitial: ", initial)
    print("\tDrop: ", drop)

# TGTTOS
def otherSide(drop):
    easyFinish = round(N - (0.95 * N))
    mediumFinish = round(N - (0.75 * N))
    hardFinish = round(N - (0.6 * N))

    a = integrate(y-(drop*x), (x,easyFinish,N))
    b = integrate(y-(drop*x), (x,mediumFinish,N))
    c = integrate(y-(drop*x), (x,hardFinish,N))

    equation = Eq(2*a+2*b+2*c, TOTAL)

    solution = solve(equation, y)
    decimal_solution = [float(sol.evalf()) for sol in solution]
    initial = round(decimal_solution[0])

    print("Get to the Other Side")
    print("\tDrop off:", drop)
    print("\tStart Value: ",initial)
    
def battleBox(deathPercentPerRound):
    rounds = teamCount
    if(N % 2 == 0):
        rounds -= 1

    winsPerRound = rounds / 2
    winsPerRound = math.ceil(winsPerRound)

    equation = Eq((rounds*x*winsPerRound)+(deathPercentPerRound*N*winsPerRound*x*(1/5)),TOTAL)
    solution = solve(equation, x)
    decimal_solution = [float(sol.evalf()) for sol in solution]
    winPoints = round(decimal_solution[0])
    killPoints = round(winPoints / 10 * 2)/2

    print("Battle Box")
    print("\tWin Points: ", winPoints)
    print("\tKill Points: " ,killPoints)

def tntRun(first,second,third):
    a = integrate(x*y, (x,1,N))
    equation = Eq(3*(a+first+second+third), TOTAL)
    solution = solve(equation, y)
    decimal_solution = [float(sol.evalf()) for sol in solution]
    survivalPoints = round(decimal_solution[0] * 2) / 2

    print("TNT Run")
    print("\tRounds: 3")
    print("\tFirst Points: ",first)
    print("\tSecond Points: ", second)
    print("\tThird Points: ", third)
    print("\tSurvival Points:", survivalPoints)




if __name__ == '__main__':
    otherSide(2)
    survivalGames(400)
    bingo()
    battleBox(0.47)
    tntRun(50,40,20)

# print(z)
