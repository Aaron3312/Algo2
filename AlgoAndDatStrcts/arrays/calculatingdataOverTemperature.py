

numOfDays = int(input("Enter the number of days: "))

tempData = list()

for i in range(numOfDays):
    tempData.append(float(input(f"Enter the temperature for day {i + 1}: ")))

def averageTemp(tempData):
    return sum(tempData) / len(tempData)

def daysAboveAverage(tempData):
    averageTemperature = averageTemp(tempData)
    daysAboveAverage = 0
    for temp in tempData:
        if temp > averageTemperature:
            daysAboveAverage += 1
    return daysAboveAverage

print(f"The average temperature is {averageTemp(tempData)}")
print(f"The number of days above average is {daysAboveAverage(tempData)}")


