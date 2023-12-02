
with open("d2_p1.in") as file:
    data = file.read().strip().split("\n")

ans = 0

for line in data:
    gameNum, gameTrailGroup = line.split(": ")
    id = int(gameNum.split()[1])     # id of the game. Like 1 in Game 1.

    possibility = True

    for gameTrail in gameTrailGroup.split("; "):
        for cubes in gameTrail.split(", "):
            num, color = cubes.split()
            num = int(num)

            if color == "green" and num > 13:
                possibility = False
            if color == "red" and num > 12:
                possibility = False
            if color == "blue" and num > 14:
                possibility = False

            
            if possibility is False:
                break
        if possibility is False:
            break
    if possibility is True:
        ans += id

print(ans)
