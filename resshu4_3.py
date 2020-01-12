import numpy as np
import random
t = []
for i in range(3):
    t.append([])
    for j in range(4):
        t[i].append(random.randint(10,99))
print(t)

people = np.sum(t, axis=1)
subject = np.sum(t, axis=0)
for i in range(3):
    print(i+1,"の点数は",people[i],"です。")

for j in range(4):
    print(j+1,"の点数は",subject[j],"です。")