#Chaz Morton Alaska Airlines coding exercise

#Input reserved seat names, separated by a space
inp = input('Please input the reserved seats: ')

#Make array of reserved seats
reserved_seats = inp.split(" ")
print(" \n Reserved Seats: ", reserved_seats, "\n")

#Create the seats in the airplane (5 rows, with seats A, B, C, D, E, F, G, H, J, K)
#A seat with value 0 means it is free, a seat with value 1 means it is taken 
rows, cols = (5, 10)
all_seats = [[0 for i in range(cols)] for j in range(rows)]
print(" \n Empty Seating Chart: \n", all_seats, "\n")

#Check if reserved seats were passed in input
if(inp != ""):
    #Loop through reserved_seats array, assign the respective seat to be reserved in all_seats (1)
    for rs in reserved_seats:
        row = int(rs[0]) - 1

        #Change letter to decimal value then subtract 65 (ex: A = 0)
        col = ord(rs[1].upper()) - 65

        #Need to adjust for skipping the letter I
        if(rs[1] == "J" or rs[1] == 'K'):
            col -= 1

        all_seats[row][col] = 1

print(" \n Seating Chart With Reserved Seats: \n", all_seats, "\n")

#Set the number of family of 4s that can fit in the remaining seats to 0
count = 0

#This represents an open section that a family can sit in 
free = [0, 0, 0, 0]

#Loop through the 5 rows
for x in range(0, 5):
    #The groups are the three ways a family of 4 can sit in an empty row
    arrangements = [all_seats[x][1:5], all_seats[x][3:7], all_seats[x][5:9]]

    #If there are no reserved seats in the row,
    #there can be two families in a row using seats in group[0] and group[2],
    #or just by one family sitting in group[1]
    if(arrangements[0] == free):
        count += 1
        if(arrangements[2] == free):
            count += 1
    elif(arrangements[1] == free):
        count += 1
    elif(arrangements[2] == free):
        count += 1

print(count, "families can fill in the remaining seats \n")


