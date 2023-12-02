gameList = []
maxRed = 12
maxBlue = 13
maxGreen = 14

gameRaw = open("input.txt", "r")

for line in gameRaw:
    gameList.append(line)

for game in gameList:
    print(game)