with open("d4.in") as file:
    data = file.read().strip().split("\n")
    #print(data)

left = []
right = []

ans = 0

for row in data:
    point = 0

    left = row.split("|")[0].split(":")[1].strip().split(" ")
    left_fix = [item for item in left if item] #remove "" item in list, convert string to int 
    #print(left_fix)
    
    right = row.split("|")[1].strip().split(" ")
    right_fix = [item for item in right if item]
    #print(right_fix)

    winNum = []
    for i in right_fix:
        for j in left_fix:
            if i == j:
                winNum.append(i)
    #print(winNum)
    if len(winNum) > 0:
        point = 2 ** (len(winNum)-1)       
        ans += point


print(ans) 
    
####### another better solution from youtube ##########
import re

with open("d4.in") as file:
    lines = file.read().strip().split("\n")

ans = 0

for line in lines:
    parts = re.split("\s+", line)  # Matches any whitespace character, such as spaces, tabs, and newlines.
    winning = list(map(int, parts[2: 12]))
    ours = list(map(int, parts[13: ]))

    score = 0
    for num in ours:
        if num in winning:
            score += 1

    if score > 0:
        ans += 2 ** (score - 1)

print(ans)