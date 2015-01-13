names = ["ppp","ooo","iii","uuu"]

noMoreSwaps = False
while noMoreSwaps == False:
    for count in range(len(names)-1):
        if names[count] > names [count+1]:
            noMoreSwaps = True
            temp = names[count]
            names[count] = names[count+1]
            names[count+1] = temp               
            noMoreSwaps = False 
            print(names)
