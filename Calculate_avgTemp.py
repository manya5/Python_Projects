numDays = int(input("How many days' temperatures? "))
total = 0
temp = []
for i in range(numDays):
    nextDay = int(input("Day " + str(i + 1) + "'s high temp: "))
    temp.append(nextDay)
    total += nextDay

avg = round(total / numDays, 2)
print("\nAverage = " + str(avg))

avg = round(total / numDays, 2)
print("\nAverage = " + str(avg))

above = 0
for i in temp:
    if i > avg:
        above += 1
print(str(above) + " days above average")