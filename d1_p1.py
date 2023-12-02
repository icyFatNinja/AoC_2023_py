with open("d1_p1.in") as file:
    data = file.read()
    #print(data)

ans = 0

data_ls = data.strip().split("\n")
#print(data_ls)

for item in data_ls:
    first = None
    last = None 
    for c in item:
        if c.isdigit():
            last = c
            if first is None:
                first = c
        
    ans += int(first + last)

print(ans)
