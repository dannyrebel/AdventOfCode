file = open('input.txt', 'r')
lines = file.readlines()



points = 0

for i in lines:
    found = []
    first_half = i[:len(i)//2]
    second_half = i[len(i)//2:]

    for char in first_half:
        for chaR in second_half:
            charVal = ord(char) - 96

            if charVal < 1:
                charVal = ord(char) - 38

            if chaR == char:
                if char not in found:
                    points += charVal
                    found.append(char)


print(points)