#Hugo
#Linear Search

def linearSearch(pizza,searchTerm):
    found = False
    count = 0

    while not found and count < len(pizza):
        if pizza[count] == searchTerm:
            found = True
            
        else:
            found = False
            
        count = count + 1
    return found

pizza = ["pepperoni", "hawaiian", "meat feast"]
searchTerm = input("What are you looking for: ")
found = linearSearch(pizza, searchTerm)
if found == True:
    print("Found")
else:
    print("Not Found")
