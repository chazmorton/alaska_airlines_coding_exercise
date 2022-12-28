#Chaz Morton Alaska Airlines coding exercise

#Input reserved seat names, separated by a space
reserved_seats = input('Please input the reserved seats: ')
print(reserved_seats)

#Create the seats in the airplane (5 rows, with seats A, B, C, D, E, F, G, H, J, K)
#A seat with value 0 means it is free, a seat with value 1 means it is taken 
rows, cols = (5, 5)
all_seats = [[0 for i in range(cols)] for j in range(rows)]
print(all_seats)

