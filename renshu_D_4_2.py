bingo = [
    [0, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0],
]
hantei =0
reachcount = 0
#横判定
for m in range(5):
    for n in range(5):
        hantei += bingo[m][n]
    if hantei == 4:
        reachcount +=1
    hantei = 0
#縦判定
for m in range(5):
    for n in range(5):
        hantei += bingo[n][m]
    if hantei == 4:
        reachcount +=1
    hantei = 0
#斜め判定\
for m in range(5):
    hantei += bingo[m][m]
if hantei == 4:
    reachcount +=1
hantei = 0
#斜め判定/
for m in range(5):
    hantei += bingo[m][4-m]
if hantei == 4:
    reachcount += 1
hantei = 0

print(reachcount)