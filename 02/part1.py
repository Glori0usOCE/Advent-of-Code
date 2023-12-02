import re

gameList = []
formattedGameList = []
maxRed = 12
maxBlue = 14
maxGreen = 13
finalCalibrationValue = 0

gameRaw = open("input.txt", "r")

for line in gameRaw:
    gameList.append(line[8:])

for game in gameList:
    formattedGameList.append(re.split('[,;]+', game))

gameIndex = 0
for game in formattedGameList:
    gameIndex += 1
    isValid = True
    for pebbles in game:
        validityCheck = ''

        for char in pebbles:
            if char.isnumeric():
                validityCheck += char

        if pebbles.find('red') != -1:
            if int(validityCheck) > maxRed:
                isValid = False

        elif pebbles.find('green') != -1:
            if int(validityCheck) > maxGreen:
                isValid = False

        elif pebbles.find('blue') != -1:
            if int(validityCheck) > maxBlue:
                isValid = False
    print(gameIndex)
    print(game)
    print(isValid)
    if isValid:
        finalCalibrationValue += gameIndex

print("Final Calibration Value: " + str(finalCalibrationValue))