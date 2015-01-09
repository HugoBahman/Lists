#Hugo
#Bubble Sort



def bubbleSort(names):
    for count in range(len(names)):
        if names[count] > names[count+1]:
            temp = names[count]
            names[count] = names[count+1]
            names[count+1] = temp
            print (names)


names = ["Hugo", "Chris", "Jordan", "Jack", "Jamie"]
bubbleSort(names)
