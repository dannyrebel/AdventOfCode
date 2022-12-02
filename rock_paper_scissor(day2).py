file = open('input.txt', 'r')
lines = file.readlines()

points = 0

for line in lines:
    turn = line[0], line[2]

    if turn[1] == "X":
        points += 1
    elif turn[1] == "Y":
        points += 2
    elif turn[1] == "Z":
        points += 3

    if turn[1] == "X" and turn[0] == "A":
        points += 3
    elif turn[1] == "Y" and turn[0] == "B":
        points += 3
    elif turn[1] == "Z" and turn[0] == "C":
        points += 3
    elif turn[1] == "X" and turn[0] == "C":
        points += 6
    elif turn[1] == "Y" and turn[0] == "A":
        points += 6
    elif turn[1] == "Z" and turn[0] == "B":
        points += 6

print(points)
