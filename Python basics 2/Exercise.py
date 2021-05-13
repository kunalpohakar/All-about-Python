#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# iterate over picture
  # if 0 -> print ''
  # if 1 -> print *

for image in picture:
  for pixels in image:
    if pixels == 1:
      print('*', end = '')
    else:
      print(' ', end = '')
    
  print(' ')
      
      
# Exercise : check Duplicates in list.
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

print(duplicates)