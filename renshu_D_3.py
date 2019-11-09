bingo = [
    [0, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0],
]
hantei = 0
bingocount = 0
# 横判定
for m in range(5):
    for n in range(5):
        if bingo[m][m] == bingo[m][n]:
            hantei += 1
    if hantei == 5 or hantei == 0:
        bingocount += 1
    hantei = 0
# 縦判定
for m in range(5):
    for n in range(5):
        if bingo[m][m] == bingo[n][m]:
            hantei += 1
    if hantei == 5 or hantei == 0:
        bingocount += 1
    hantei = 0

# 斜め判定\
for n in range(5):
    if bingo[0][0] == bingo[n][n]:
        hantei += 1
if hantei == 5 or hantei == 0:
    bingocount += 1
hantei = 0
# 斜め判定/
for n in range(5):
    if bingo[0][4] == bingo[n][4 - n]:
        hantei += 1
if hantei == 5 or hantei == 0:
    bingocount += 1
hantei = 0


print(bingocount)
