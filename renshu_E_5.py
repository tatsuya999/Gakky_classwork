coods = [
    {"name": "あだち", "x": 3, "y": 0},
    {"name": "いしだ", "x": 5, "y": 3},
    {"name": "うえの", "x": 0, "y": 4},
    {"name": "えぐち", "x": 6, "y": 5},
    {"name": "おくだ", "x": 2, "y": 8},
]
sums = []
maxs = []
for m in range(len(coods)):
    sums.append(0)
    maxs.append(0)
    for n in range(len(coods)):
        distance = abs(coods[m]["x"] - coods[n]["x"]) + abs(
            coods[m]["y"] - coods[n]["y"]
        )
        sums[m] += distance
        if distance > maxs[m]:
            maxs[m] = distance

    print(coods[m]["name"] + "への距離の合計移動距離は" + str(sums[m]) + "です")
    print(coods[m]["name"] + "への距離の最大移動距離は" + str(maxs[m]) + "です")

minsum = sums[0]
for m in range(len(sums)):
    if minsum > sums[m]:
        minsum = sums[m]

minmax = maxs[0]
for m in range(len(maxs)):
    if minmax > maxs[m]:
        minmax = maxs[m]
print("合計移動距離の最小値は" + str(minsum) + "です")
print("最大移動距離の最小値は" + str(minmax) + "です")

