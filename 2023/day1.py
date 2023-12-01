#!/usr/bin/python3

import re

file = open("day1_input", "r")
lines = file.readlines()

reg = re.compile("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", re.IGNORECASE)

number_dict = {'one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9'}

total = 0
for line in lines:
    nums = re.findall(reg, line)
    index = [0, len(nums)-1]
    firstNum = nums[index[0]]
    secondNum = nums[index[1]]
    if not firstNum.isnumeric():
        firstNum = ''.join(number_dict[each] for each in firstNum.split())
    if not secondNum.isnumeric():
        secondNum = ''.join(number_dict[each] for each in secondNum.split())
    number = firstNum + secondNum
    # print("Line: ", line.rstrip(), "\nNums:", nums, "\nNumber: ",number, "\n")
    total += int(number)
print("Total: ", total)
