#Hugo
#2D List K:D

players = [
    ["k1llmAchine",51,49],
    ["bob2247",5,99],
    ["hAxOr12",72,30]
]

print("-"*24)
for player in players:
    print("|{0:<12}|{1:^4}|{2:^4}|".format(player[0], player [1], player[2]))
    print("-"*24)
