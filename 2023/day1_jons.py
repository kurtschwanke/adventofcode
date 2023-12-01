#!/usr/bin/python3

input = open("day1_input", "r")
data = input.readlines()

result = []
numberStrings = ["one","two","three","four","five","six","seven","eight","nine"]
for line in range(len(data)):
    curNumbers = []
    for x in range(len(data[line])):
        #print(f"Number Check: {data[line][x]}")
        if data[line][x].isnumeric():
            curNumbers.append(data[line][x])
            #print(f"Number Found: {data[line][x]}")
        for num in range(len(numberStrings)):
           # print(f"Scan Location: {x}:{x+len(numberStrings[num])}")
            if data[line][x:x+len(numberStrings[num])] == numberStrings[num]:
                #print(f"Word Found: {numberStrings[num]}, Appending: {num+1}")
                curNumbers.append(str(num+1))
    #print(f"curNumbers: {curNumbers}")
    result.append(int(curNumbers[0] + curNumbers[len(curNumbers)-1]))
#print(f"result: {result}")
sum = 0
for num in result:
    sum += num
print(f"The sum of calibrations is: {sum}")
