#Hugo
#2D List K:D

players = [
    ["k1llmAchine",51,49],
    ["bob2247",5,99],
    ["hAxOr12",72,30]
]

print("{0:<12}  {1:^6}  {2:>5}".format("Player","Kills","Deaths"))


for count in range(4):
    print("{0:<12}".format(players[count][0]))
    
