#!/usr/bin/python3

# This is really horrible

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
    red=0
    blue=0
    green=0
    for game in gameSet:
      print(game)
      cubes = game.split(',')
      for cube in cubes:
        cube = cube.strip()
        c = cube.split(' ')
        id = int(c[0])
        colour = c[1]
        if colour == 'red':
          if red == 0:
            red = id
          elif id > red:
            red = id
          #if id > 12:
            #raise EscapeLoop
        elif colour == 'blue':
          if blue == 0:
            blue = id
          elif id > blue:
            blue = id
          #if id > 14:
            #raise EscapeLoop
        elif colour == 'green':
          if green == 0:
            green = id
          elif id > green:
            green = id
          #if id > 13:
            #raise EscapeLoop
        else:
          raise EscapeLoop
  except EscapeLoop:
    continue
  power = red * green * blue
  # print(power)
  # total += int(gameId[0])
  total += power

print(total)
