file = open("input_1.txt")

total=0

23-25,20-22
20-22,23-25
20-25
49-93,45-49         
36-86,37-81
30-73,73-81
42-46,38-56
"16-96,15-95"
["16-96"]    
[""]
for line in file:
    pair = line.split(",")
    first_extremities = pair[0].split("-")
    second_extremities = pair[1].split("-")
    
    first_extremities[0] = int(first_extremities[0])
    first_extremities[1] = int(first_extremities[1])
    second_extremities[0] = int(second_extremities[0])
    second_extremities[1] = int(second_extremities[1])
    
    second_distance_from_begin = second_extremities[1] - second_extremities[0]
    first_distance_from_begin  = first_extremities[1]  - first_extremities[0]
    
    if (first_extremities[0] > second_extremities[0]):
        between = first_extremities[0] - second_extremities[0]
        if (between <= second_distance_from_begin):
            total += 1
            
    elif (first_extremities[0] < second_extremities[0]):
        between = second_extremities[0] - first_extremities[0]
        if (between <= first_distance_from_begin):
            total += 1
    elif (first_extremities[0] == second_extremities[0]):
            total += 1             
    
            
print(total)  