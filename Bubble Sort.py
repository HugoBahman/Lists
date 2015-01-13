#Hugo
#Bubble Sort

def userInput():
    names = []
    switch = False
    while switch == False:
        userInput = input("Please enter a name ('stop' to stop): ")
        if userInput == "stop":
            switch = True
        else:
            names.append(userInput)
    return names
            
def bubbleSort(userInput):
    noMoreSwaps = False
    while noMoreSwaps == False:
        for count in range(len(names)-1):
            if names[count] > names [count+1]:
                noMoreSwaps = True
                temp = names[count]
                names[count] = names[count+1]
                names[count+1] = temp
                print(names)
            noMoreSwaps = False 



names = userInput()
bubbleSort(userInput)



