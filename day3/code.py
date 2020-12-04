
def s(dx,dy):
  with open("day3/input.txt") as file:
      map = [x for x in file.read().split("\n")[::dy]]


  treeCount = 0
  x = 0

  for row in map:
      try:
          treeCount += (row[x % (len(map[0]))] == "#")
          x += dx
      except IndexError:
          print('null')

  return treeCount


treeCount = 1
slopes= [(1,2)]

for slope in slopes :
    treeCount*=s(slope[0],slope[1])

print(treeCount)
