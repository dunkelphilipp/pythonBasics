calPerMin = 4.2
time = 0
calBurned = 0.0

for time in range(10, 31, 5):
    calBurned = calPerMin * time
    print(time, calBurned)
