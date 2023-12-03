with open("d3_p1.in") as file:
    data = file.read().strip().split("\n")
    #print(data)


numRow = len(data)
numCol = len(data[0])

def isValidSymbol(indexOfRow, indexOfCol):
    if not (0 <= indexOfRow < numRow and 0 <= indexOfCol < numCol):
        return False
    
    return data[indexOfRow][indexOfCol] != "." and not data[indexOfRow][indexOfCol].isdigit()

ans = 0

for rowIndex, row in enumerate(data):
    firstIndex = 0
    CurrentIndex = 0 

    while CurrentIndex < numCol:
        firstIndex = CurrentIndex #for starting of each number: 25, 65
        num = ""
        while CurrentIndex < numCol and row[CurrentIndex].isdigit(): #handles digits
            num += row[CurrentIndex]
            CurrentIndex += 1

        if num == "":   #Handles the symbols. Without this i+=1 is not executed in previsou while when it is a symbol and it will be an infinit whole loop.
            CurrentIndex += 1
            continue
        #go back to parent while after t.ex. ...625

        num = int(num)
    
        if isValidSymbol(rowIndex, firstIndex - 1) or isValidSymbol(rowIndex, CurrentIndex):
            ans += num
            continue

        for colIndex in range(firstIndex - 1, CurrentIndex + 1):
            if isValidSymbol(rowIndex - 1, colIndex) or isValidSymbol(rowIndex + 1, colIndex):
                ans += num
                break 

print(ans)












