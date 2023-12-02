with open("d1_p2.in") as file:
    data = file.read()
    #print(data)


# data = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen"""

ans = 0

data_ls = data.strip().split("\n")
#print(data_ls)

keyValue = {
        "zero":0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

for item in data_ls:
    
    first = None
    last = None
    s = ""

    for c in item:
        digit = None
        if c.isdigit():
            digit = c
        else:
            s += c
            for key, value in keyValue.items():
                if s.endswith(key):
                    digit = str(value)
        if digit is not None:
            last = digit
            if first is None:
                first = digit
       
    #print(int(first + last))
    ans += int(first + last)

print(ans)







