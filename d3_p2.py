with open("d3_p2.in") as file:
    data = file.read().strip().split("\n")

numRow = len(data)
numCol = len(data[0])
rowIndex = 0
colIndex = 0

#start from numbers that have symbols around. Find all the symbols and filter out the *.
#in all the adjacent positions of a number, if *, put the corresponding number to grid cell. append the cell for more *.

#create a grid or matrix with 140 rows and 140 columns, where each cell is initially empty. Each cell is a list. 

grid = [[[] for _ in range(numCol)] for _ in range(numRow)] 

def isGear(i, j, num):
    if not (0 <= i < numRow and 0 <= j < numCol):
        return False
    
    if data[i][j] == "*":
        grid[i][j].append(num)
    return data[i][j] != "." and not data[i][j].isdigit()

ans = 0

for i, row in enumerate(data): #Iterate y-axis
    first = 0
    current = 0

    while current < numCol:
        first = current
        num = ""
        while current < numCol and row[current].isdigit(): #iterate x-axis
            num += row[current]
            current += 1

        if num == "":
            current += 1
            continue #continue is necessary for int method 

        num = int(num) 

        #following steps check all the adjacent positions of a number once a num is set with a value.          
        isGear(i, first - 1, num) or isGear(i, current, num) #remeber current += 1 in previous step

        for x in range(first - 1, current + 1):
            isGear(i - 1, x, num) or isGear(i + 1, x, num)

for m in range(numRow):
    for n in range(numCol):
        nums = grid[m][n] #list
        if data[m][n] == "*" and len(nums) == 2:
            ans += nums[0] * nums[1]

print(ans)




























# for r, row in enumerate(grid):
#     for c, ch in enumerate(row):
#         if ch != "*":
#             continue

#         cs = set()

#         for cr in [r - 1, r, r + 1]:
#             for cc in [c - 1, c, c +1]:
#                 if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
#                     continue
#                 while cc > 0 and grid[cr][cc - 1].isdigit():
#                     cc -= 1
#                 cs.add((cr, cc))

# ns = []

# for r, c in cs















# ans = 0
# numList = []

# def isValidGear(indexOfRow, indexOfCol):
#     if not (0 <= indexOfRow < numRow and 0 <= indexOfCol < numCol):
#         return False
    
#     if data[indexOfRow][indexOfCol-1].isdigit or data[indexOfRow][indexOfCol-1].isdigit:
#         numList.append(data[i][j])
#         for j in range(colIndex - 1, colIndex + 2):
#             if data[i][j].isdigit():
#                 numList.append(data[i][j])
    
#     if len(numList) == 2:
#         return numList
                

# for row in data:
#     #print(row)
#     for n, element in enumerate(row):
#         if element == "*":
#             rowIndex = data.index(row)
#             colIndex = n
#            #print(rowIndex, colIndex)

#             isValidGear(rowIndex, colIndex)
#             print(numList)

       

