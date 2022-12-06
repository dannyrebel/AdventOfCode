file = open('input.txt', 'r')
lines = file.readlines()

count = 0
points = 0
first_line = ""
found = []

for i in lines:

    count += 1

    if count == 1:
        first_line = i.strip()
    elif count == 2:
        for char in i.strip():
            if char in first_line:
                if char not in found:
                    found.append(char)
    else:
        for three in i.strip():
            if three in found:
                charVal = ord(three) - 96
                if charVal < 1:
                    charVal = ord(three) - 38
                points += charVal
                found.remove(three)
        count = 0
        found = []
print(points)
