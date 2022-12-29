#Chaz Morton Alaska Airlines coding exercise

#Input reserved seat names, separated by a space
inp = input('Please input the reserved seats: ')

#Make array of reserved seats
reserved_seats = inp.split(" ")
print(reserved_seats)

#Create the seats in the airplane (5 rows, with seats A, B, C, D, E, F, G, H, J, K)
#A seat with value 0 means it is free, a seat with value 1 means it is taken 
rows, cols = (5, 10)
all_seats = [[0 for i in range(cols)] for j in range(rows)]
print(all_seats)

#Loop through reserved_seats array, assign the respective seat to be reserved in all_seats (1)
for rs in reserved_seats:
    row = int(rs[0]) - 1
    #Change letter to decimal value then subtract 65 (ex: A = 0)
    col = ord(rs[1]) - 65

    all_seats[row][col] = 1

print(all_seats)

#Set the number of family of 4s that can fit in the remaining seats to 0
count = 0

#This represents an open section that a family can sit in 
free = [0, 0, 0, 0]

#Loop through the 5 rows
for x in range(0, 5):
    #The groups are the three ways a family of 4 can sit in an empty row
    groups = [all_seats[x][1:5], all_seats[x][3:7], all_seats[x][5:9]]

    #If there are no reserved seats in the row,
    #there can be two families in a row using seats in group[0] and group[2],
    #or just by one family sitting in group[1]
    if(groups[0] == free):
        count += 1
        if(groups[2] == free):
            count += 1
    elif(groups[1] == free):
        count += 1
    elif(groups[2] == free):
        count += 1

print(count, "families can fill in the remaining seats")


