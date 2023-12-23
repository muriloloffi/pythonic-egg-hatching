matrix = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

picture = ''
count = 0
for row in matrix:
  for numbr in row:
    if numbr == 0:
      picture += ' '
    if numbr == 1:
      picture += '*'
  if count < (len(matrix) - 1):
    picture += '\n'
    count += 1

print(picture)
