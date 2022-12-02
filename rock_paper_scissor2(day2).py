file = open('input.txt', 'r')
lines = file.readlines()

points = 0

for line in lines:
    turn = line[0], line[2]

    #win possibility
    if turn[0] == "A" and turn[1] == "Z":
        points += 8
    elif turn[0] == "B" and turn[1] == "Z":
        points += 9
    elif turn[0] == "C" and turn[1] == "Z":
        points += 7

    #draw possibility
    elif turn[0] == "A" and turn[1] == "Y":
        points += 4
    elif turn[0] == "B" and turn[1] == "Y":
        points += 5
    elif turn[0] == "C" and turn[1] == "Y":
        points += 6

    #lose possibility
    elif turn[0] == "A" and turn[1] == "X":
        points += 3
    elif turn[0] == "B" and turn[1] == "X":
        points += 1
    elif turn[0] == "C" and turn[1] == "X":
        points += 2

print(points)