#this solution is from youtube 
#https://www.youtube.com/watch?v=QpPsyMEYAV8

import re

with open("d4.in") as file:
    data = file.read().strip().split("\n")

rowNum = len(data)

#create empty list copies which contains rowNum + 1 sublists. 
copies = [[] for _ in range(rowNum + 1)]

for i, row in enumerate(data):
    #print(row)
    parts = re.split("\s+", row)
    #print(parts)
    index = parts.index("|")
    left = parts[2: index]
    right = parts[index + 1:]

    point = 0
    for m in right:
        if m in left:
            point += 1

    for n in range(i + 1, i + 1 + point): #copied cards 
        copies[i].append(n)

point = [0] + [1 for _ in range(rowNum)]

for i in range(rowNum - 1, -1, -1):
    for j in copies[i]:
        point[i] += point[j]

#print(copies)
#print(point)

print(sum(point))