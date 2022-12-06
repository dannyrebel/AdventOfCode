file = open("input.txt", 'r')
lines = file.readlines()

points = 0

for line in lines:

    [first_range, second_range] = line.split(",")
    [first_start, first_end] = first_range.split("-")
    [second_start, second_end] = second_range.split('-')

    if int(first_start) <= int(second_start) and int(first_end) >= int(second_end):
        points += 1
    elif int(first_start) >= int(second_start) and int(first_end) <= int(second_end):
        points += 1
    elif int(first_start) <= int(second_start) <= int(first_end):
        points += 1
    elif int(first_start) >= int(second_start) >= int(first_end):
        points += 1
    elif int(first_start) <= int(second_end) <= int(first_end):
        points += 1
    elif int(first_start) >= int(second_end) >= int(first_end):
        points += 1

print(points)

