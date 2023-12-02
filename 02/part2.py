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



print("Final Calibration Value: " + str(finalCalibrationValue))