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
        print(
            "{}から{}までの距離は{}です".format(
                coods[m]["name"],
                coods[n]["name"],
                abs(coods[m]["x"] - coods[n]["x"]) + abs(coods[m]["y"] - coods[n]["y"]),
            )
        )

