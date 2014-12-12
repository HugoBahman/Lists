#Hugo
#Task 1 Improvement

values = []

for count in range(4):
    value = int(input("Enter your first number: "))
    values.append(value)

result = 0
index = 0

for count in range(4):
    index = index + 1
    if result < values[index]:
        result = values[index]
    
