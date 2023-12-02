#!/usr/bin/python3

import re

class EscapeLoop( Exception ):
    pass

reg = re.compile("Game ([0-9]{1,})", re.IGNORECASE)

file = open("day2_input", "r")
lines = file.readlines()
total = 0
count = 0
for line in lines:
  try:
    gameId = re.findall(reg, line)
    modLine = re.sub(reg, '', line)
    modLine = modLine.strip(':')
    modLine = modLine.strip('\n')
    gameSet = modLine.split(';')
    count+=1
    for game in gameSet:
      cubes = game.split(',')
      for cube in cubes:
        cube = cube.strip()
        c = cube.split(' ')
        id = int(c[0])
        colour = c[1]
        if colour == 'red':
          if id > 12:
            raise EscapeLoop
        elif colour == 'blue':
          if id > 14:
            raise EscapeLoop
        elif colour == 'green':
          if id > 13:
            raise EscapeLoop
  except EscapeLoop:
    continue
  total += int(gameId[0])

print(total)
