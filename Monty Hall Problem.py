# xperimental simulation of the monty hall problem

import random
woc = 0
wc = 0
for _ in range(1000000):
    arr = [1, 2, 3]
    prize = random.choice(arr)
    fc = random.choice(arr)
    if(fc == prize):
        arr.remove(fc)
        arr.remove(random.choice(arr))
        arr.append(fc)
    else:
        arr = fc+prize
    sc = prize
    if(fc == prize):
        woc += 1
    elif(sc == prize):
        wc += 1
print("Without change", woc/10000)
print("With change", wc/10000)
