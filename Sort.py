#Hugo
#Bubble Sort

def bubbleSort(names):
    for count in range(len(names)-1):
        if names[count] > names[count+1]:
            temp = names[count]
            names[count] = names[count+1]
            names[count+1] = temp
            print("{0}".format(names))

names = ["Hugo", "Chris", "Jordan", "Jack", "Jamie"]
print(names)
bubbleSort(names)
