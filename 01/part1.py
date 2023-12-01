textLines = []
calibrationValues = []
newTextLines = []
newCalibrationValues = []
finalCalibrationValue = 0


textFile = open('input.txt', 'r')

for x in textFile:
    textLines.append(x)

for line in textLines:
    calibrationValue = 0
    tempLineArray = []
    print("Line: " + line)
    for char in line:
        if char.isnumeric():
            tempLineArray.append(char)

    if len(tempLineArray) == 1:
        calibrationValue = tempLineArray[0]
        calibrationValue += tempLineArray[0]

    else:
        calibrationValue = tempLineArray[0]
        calibrationValue += tempLineArray[len(tempLineArray)-1]
        
    print("Calibration Value: " + calibrationValue)
    calibrationValues.append(calibrationValue)

for value in calibrationValues:
    finalCalibrationValue += int(value)

print("Final Calibration Value: " + str(finalCalibrationValue))