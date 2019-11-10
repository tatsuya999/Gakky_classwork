coods = [
    {"name": "あだち", "x": 3, "y": 0},
    {"name": "いしだ", "x": 5, "y": 3},
    {"name": "うえの", "x": 0, "y": 4},
    {"name": "えぐち", "x": 6, "y": 5},
    {"name": "おくだ", "x": 2, "y": 8},
]

for m in range(len(coods)):
    sum = 0
    max = 0

    for n in range(len(coods)):
        distance = abs(coods[m]["x"] - coods[n]["x"]) + abs(
            coods[m]["y"] - coods[n]["y"]
        )

        sum += distance
        if distance > max:
            max = distance

    print(coods[m]["name"] + "への距離の最大値は" + str(max) + "です")
    print(coods[m]["name"] + "への距離の平均値は" + str(sum / 4) + "です")
