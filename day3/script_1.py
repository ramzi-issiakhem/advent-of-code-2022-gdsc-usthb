file = open("input_1.txt")

def calculate_priority(car):
    if ( ord(car) < ord("a")):
        return (ord(car) - 38)
    else:
        return (ord(car) - 96)

total =0
    
for line in file:
    line = line[0:(len(line) - 1)]
    len_line = len(line)
    middle = int(len_line / 2)
    first_backpack = line[0:middle]
    second_backpack = line[middle:len_line]
    common_letter = ""
    
    for i in first_backpack:
        if i in second_backpack:
            priority = calculate_priority(i)
            total += priority
            break
            
print(total)  