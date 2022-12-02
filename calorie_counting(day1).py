import sys

file = open('input.txt', 'r')
lines = file.readlines()

elf = 0
max_elf = -sys.maxsize

for i in lines:

    if i == "\n":
        if elf > max_elf:
            max_elf = elf
        elf = 0
        continue

    elf += int(i)

print(max_elf)
