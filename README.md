# Chaz Morton Alaska Airlines Coding Exercise

## Questions:

- In what ways can you arrange a family of 4 in an empty row with the given specifications?
- How can my program tell if a family is sitting together but split by an aisle? 
- Do seats in column A or K ever need to be looked at?
- What is the maximum amount of four-person families with all empty rows?
- What Data Structures can I utilize to make an efficient solution?

## Assumptions: 

- The input is in the correct format (separated by spaces, with row first then column second, ex: "1A 2F").
- There are no repeats of seats in the input.
- Seats cannot be assigned to more than one person, meaning four-person families cannot overlap seats.

## Potential Paths for a Solution: 

- Originally, I was thinking of counting each individual seat until it added up to 4. I would have to check if the family of four was sitting across an aisle, and if they are, is the family split into 3-1 or 2-2. I could check this by creating a graph, where each node is a seat and has edges connected to the seat/node next to it on the seating chart. If two nodes represent seats that are separated by an aisle, the edge would have a weight of 1. If the seats were next to together as normal, then the edge between the two seats will have a weight of 0. This makes it possible for us to tell if two seats are sitting across an aisle. Then, if those two nodes connected by the edge with weight 1 are free, we can consider these two spots as free. We then check if these two nodes are both connected to an additional free node. If so, then this will represent as a 2-2 split spot across an aisle that the family can sit at. 

- This second potential path is the solution that I implemented, which is more efficient to use. I used arrangements, which are groups of 4-seats where it is viable for the four-person family to sit. There are three arrangements total for a family of four when checking any row. As explained below, this means that there is a maximum of three comparisons per row between our arrangements and our "free" array. This is faster and more simple to implement than the previous path. 

## Final Solution:

First, we look at all the possible ways a four-person family can fit into an empty row. There are three different arrangements a four-person family can sit in. These are named Arrangement 1, Arrangement 2 and Arrangement 3. Arrangement 1 consists of seats B, C, D, E. Arrangement 2 consists of seats D, E, F, G. Arrangement 3 consists of seats F, G, H, J. 

![Image 1](images/Alaska%20Image%201-1.jpg)

It is given that the four-person family must be sitting together. For example, the family members can sit together in Arrangement 2 in the middle of the plane. The family is able to sit next together and be separated by an aisle, but only if the family has two people sitting together on each side of the aisle. Two examples of this instance are Arrangement 1 and Arrangement 3. The family is not able to be split into 3 and 1 across an aisle. For example, a four-person family sitting in seats A, B, C and D is not viable. This is the same with a four-person family sitting in seats G, H, J and K.

![Image 1](images/Alaska%20Image%202-1.jpg)

The seats in columns A and K are only important if one of four family members is sitting in them. Though if this is the case, this will result into a 3-1 split of the four-person family across an aisle, which as just discussed is not viable. This means that we can ignore looking at seats in column A and column K. 

The next question is how can we maximize the amount of four-person families sitting in an empty row? There are two different options using the combination of these three arrangements. These possibilities are seen as below: 

![Image 1](images/Alaska%20Image%203-1.jpg)

With an empty row, the combination that maximizes the amount of four-person families is using sitting both Arrangement 1 and Arrangement 3. Giving us 2 four-person families in an empty row. 

Now we take a look if we have reserved seats in the row. The seating chart for Alaska's new commuter plane is represented as a 2D array, with 5 rows and 10 columns. Initially, all the seats have a value of 0, meaning that they are vacant. If a seat has a value of 1, then it is occupied. 

Given the input of reserved seats, we change the values of the respective seats to 1 to indicate they are reserved. There is an array created named "free", with length four of values of all 0s. We use this "free" array as a representation of four vacant seats, in which we compare each of our arrangements to. 

With the reserved seats now in our seating chart, we take a look at our given row, starting at row 1. We grab our three arrangements from that row, Arrangement 1, Arrangement 2, and Arrangement 3, using this in our code: `arrangements = [all_seats[x][1:5], all_seats[x][3:7], all_seats[x][5:9]]`

In this sample row,
![Image 1](images/Alaska%20Image%204-1.jpg)

we are given the arrangements: ![Image 1](images/Alaska%20Image%205-1.jpg)

First we start by comparing Arrangment 1 with "free". Arrangement 1 is equal to "free", this means we can sit the family there and so we increment our count of four-person families by doing count += 1. Then, we skip Arrangment 2 (since Arrangement 1 overlaps in seats) and check Arrangement 3. We compare Arrangment 3 to "free". Unfortunatly, these do not match, so we conclude our check with this row. 

In this sample row, 
![Image 1](images/Alaska%20Image%206-1.jpg)

we are given the arrangments: ![Image 1](images/Alaska%20Image%207-1.jpg)

Arrangement 1 does not equal "free", so we look at Arrangment 2. Arrangment 2 is equal to "free", so we increment count by 1. Since Arrangement 2 and Arrangement 3 have overlapping seat, we do not need to check Arrangment 3. 

The code for these checks is as below: 

    if(arrangements[0] == free):
        count += 1
        if(arrangements[2] == free):
            count += 1
    elif(arrangements[1] == free):
        count += 1
    elif(arrangements[2] == free):
        count += 1

We do these checks in each row, using a for loop to go through rows 1 - 5. Each time a four-person family is seated, we increment our count by 1. When the 5th row is finally checked, our count represents the maximum total amount of four-person families we can seat. 
