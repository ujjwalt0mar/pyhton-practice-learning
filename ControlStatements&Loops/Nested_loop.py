# for x in range(0, 5):
#     for y in range(0, 5):
#         print(x,',', y) 

cordinates = []

for x in range(0, 5):
    for y in range(0, 5):
       c = str(x) + ',' + str(y)
       cordinates.append(c)
print(cordinates)