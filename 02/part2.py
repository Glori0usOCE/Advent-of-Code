import re

gameList = []
formattedGameList = []
setPower = []
finalCalibrationValue = 0

gameRaw = open("input.txt", "r")

for line in gameRaw:
    gameList.append(line[8:])

for game in gameList:
    formattedGameList.append(re.split('[,;]+', game))

for game in formattedGameList:
    minRed = 0
    minBlue = 0
    minGreen = 0
    power = 0
    for pebbles in game:
        validityCheck = ''

        for char in pebbles:
            if char.isnumeric():
                validityCheck += char

        if pebbles.find('red') != -1:
            if int(validityCheck) > minRed:
                minRed = int(validityCheck)

        elif pebbles.find('green') != -1:
            if int(validityCheck) > minGreen:
                minGreen = int(validityCheck)

        elif pebbles.find('blue') != -1:
            if int(validityCheck) > minBlue:
                minBlue = int(validityCheck)
    power = minRed * minGreen * minBlue
    setPower.append(power)

for power in setPower:
    finalCalibrationValue += power


print("Final Calibration Value: " + str(finalCalibrationValue))