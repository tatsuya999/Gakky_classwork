coods = [
    {"name": "あだち", "x": 3, "y": 0},
    {"name": "いしだ", "x": 5, "y": 3},
    {"name": "うえの", "x": 0, "y": 4},
    {"name": "えぐち", "x": 6, "y": 5},
    {"name": "おくだ", "x": 2, "y": 8},
]
result = []
for m in range(len(coods)):
    for n in range(m + 1, len(coods)):
        result.append(
            [
                coods[m]["name"],
                coods[n]["name"],
                abs(coods[m]["x"] - coods[n]["x"]) + abs(coods[m]["y"] - coods[n]["y"]),
            ]
        )
print(result)

sum = 0
max = 0
for m in range(4):
    distance = abs(coods[m]["x"] - coods[4]["x"]) + abs(coods[m]["y"] - coods[4]["y"])
    sum += distance
    if distance > max:
        max = distance

print("おくだへの距離の最大値は" + str(max) + "です")
print("おくだへの距離の平均値は" + str(sum / 4) + "です")
