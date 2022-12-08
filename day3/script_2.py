

file = open("input_1.txt")

def calculate_priority(car):
    if ( ord(car) < ord("a")):
        return (ord(car) - 38)
    else:
        return (ord(car) - 96)

total =0
i=0    
temp = []
groups = []

for line in file:
    line = line[0:len(line)-1]
    temp.append(line)
    if (i == 2 ):
        groups.append(temp)    
        temp = []
        i = -1
    i += 1

common_letter = ""
for i in groups:
    for j in i[0]:
        if j in i[1] and j in i[2]:
            total += int(calculate_priority(j))
            break
print(total)             
    
            
 