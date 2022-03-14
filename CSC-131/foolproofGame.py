from random import randint

gameNum = int(input("How many games? "))
coinFlips = int(input("How many coin tosses per game? "))
aDubs = 0
bDubs = 0
profDubs = 0

for game in range(1, gameNum + 1):
    grpA = 0
    grpB = 0
    prof = 0
    print(f"Game: {game}")
    for __ in range(1, coinFlips + 1):
        coin1 = randint(0,1)
        coin2 = randint(0,1)
        if coin1 == 1 and coin2 == 1:
            grpA += 1
        elif coin2 == 0 and coin1 == 0:
            grpB += 1
        else:
            prof += 1
    print(f"Group A: {grpA} ({grpA/coinFlips*100}%); Group B: {grpB} ({grpB/coinFlips*100}%); Prof: {prof} ({prof/coinFlips*100}%)")
    if prof > grpA and prof > grpB:
        profDubs += 1
    elif grpA > prof and grpA > grpB:
        aDubs += 1
    else:
        bDubs += 1

print(f"Wins: Group A = {aDubs} ({aDubs/gameNum*100}%); Group B = {bDubs} ({bDubs/gameNum*100}%); Prof = {profDubs} ({profDubs/gameNum*100}%)")

