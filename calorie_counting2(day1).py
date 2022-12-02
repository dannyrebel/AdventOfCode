import sys

file = open('sample.txt', 'r')
lines = file.readlines()

elf = 0
first_elf = -sys.maxsize
second_elf = -sys.maxsize
third_elf = -sys.maxsize

for i in lines:

    if i == "\n": #40
        if elf > first_elf: #30
            third_elf = second_elf
            second_elf = first_elf
            first_elf = elf
        elif elf > second_elf: #10
            third_elf = second_elf
            second_elf = elf
        elif elf > third_elf:
            third_elf = elf
        elf = 0
        continue

    elf += int(i)

print(first_elf)
print(second_elf)
print(third_elf)
