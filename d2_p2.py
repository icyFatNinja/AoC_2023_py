with open("d2_p2.in") as file:
    data = file.read().strip().split("\n")

ans = 0

for line in data:
    gameNum, gameTrailGroup = line.split(": ")
    
    greenList = []
    redList = []
    blueList = []

    for gameTrail in gameTrailGroup.split("; "):
        for cubes in gameTrail.split(", "):
            num, color = cubes.split()
            num = int(num)

            if color == "green":
                greenList.append(num)
            if color == "red":
                redList.append(num)
            if color == "blue":
                blueList.append(num)

    powerOfEachGame = max(greenList) * max(redList) * max(blueList)
    ans += powerOfEachGame

print(ans)



    # print(greenMaxNumEachGame)
    # print(redMaxNumEachGame)
    # print(blueMaxNumEachGame)

    # print(greenList)
    # print(redList)
    # print(blueList)