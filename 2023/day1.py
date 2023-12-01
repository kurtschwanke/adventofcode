#!/usr/bin/python3
# import os
import re

# read each line from input
# filter for numbers
# create two digit number from first and last number in line (duplicate if only 1 number)
# sum together

file = open("day1_input", "r")
lines = file.readlines()

reg = re.compile("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", re.IGNORECASE)
regexDigit = re.compile("[0-9]")

number_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

total = 0
for line in lines:
    print(line)
    nums = re.findall(reg, line.rstrip())
    print(re.findall(reg, line))
    # break
    index = [0, len(nums)-1]
    firstNum = nums[index[0]]
    secondNum = nums[index[1]]
    if not re.match(regexDigit, firstNum):
        firstNum = ''.join(number_dict[ele] for ele in firstNum.split())
    if not re.match(regexDigit, secondNum):
        secondNum = ''.join(number_dict[ele] for ele in secondNum.split())
    number = firstNum + secondNum
    print("Line: ", line.rstrip(), "\nNums:", nums, "\nNumber: ",number, "\n")
    total += int(number)
print("Total: ", total)

