#Hugo
#Random Number Selector

import random

fullList = []

for count in range(1,20):
    fullList.append(count)

numbersPicked = 0
while numbersPicked != 6:
    number = random.choice(fullList)
    if number != 0:
        print (number)
        fullList.pop(number-1)
        fullList.insert(number-1,0)
        numbersPicked = numbersPicked + 1

print(fullList)
        

