textLines = []
calibrationValues = []
newTextLines = []
finalCalibrationValue = 0


textFile = open('input.txt', 'r')
#newTextFile = open('newinput.txt', 'w')

for x in textFile:
    textLines.append(x)

for value in textLines:
    newValue = value
    newValue = newValue.replace('nine', 'n9e')
    newValue = newValue.replace('eight', 'e8t')
    newValue = newValue.replace('seven', 's7n')
    newValue = newValue.replace('six', 's6x')
    newValue = newValue.replace('five', 'f5e')
    newValue = newValue.replace('four', 'f4r')
    newValue = newValue.replace('three', 't3e')
    newValue = newValue.replace('two', 't2o')
    newValue = newValue.replace('one', 'o1e')

    newTextLines.append(newValue)
    #newTextFile.write(newValue)

for line in newTextLines:
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
#newTextFile.close()

#def 