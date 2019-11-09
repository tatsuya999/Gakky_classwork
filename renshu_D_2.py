bingo = [
    [0, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0],
]

hantei = 0

for m in range(5):
    for n in range(5):
        if bingo[m][m] == bingo[n][m]:
            hantei += 1
    if hantei == 5:
        print(str(m))
    hantei = 0

