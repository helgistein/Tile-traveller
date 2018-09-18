#1. Declare all variables that will be used in the excercise
#2. Design how the grid is setup
#3. Figure out how the player will move
#4. code how the player and the grid will interact.
#5. set boundaries as to where the player can and can not move
#6. Make it so the player will be able to go back and forth 

#n/N up
#e/E right
#s/S down
#w/W left
#You can travel: (N)orth.
#Direction: s
#Not a valid direction!
#Direction: n
#You can travel: (N)orth or (E)ast or (S)outh.
#Direction: N
#reytur 1,1 möguleikar n/N up
#reytur 1,2 möguleikar n/N up, e/E right, s/S down
#reytur 1,3 möguleikar e/E right, s/S down
#reytur 2,1 möguleikar n/N up
#reytur 2,2 möguleikar w/W left, s/S down
#reytur 2,3 möguleikar e/E right, w/W right
#reytur 3,1 möguleikar n/N up
#reytur 3,2 möguleikar n/N up, s/S down
#reytur 3,3 möguleikar s/S down, w/W left

north = "(N)orth"
south = "(S)outh"
east = "(E)ast"
west = "(W)est"

i = 1
j = 1

location = (i, j)
while i != 3 and j != 1:

    print("You can travel: (N)orth")
    direction = input("Direction: ")
    while direction == ("s", "e", "w"):
        direction = input("Direction: ")

    if direction == "n":
        j += 1
    else:
        print("Not a valid direction!")

    elif i == 1 and j == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh. ")
        direction = input("Direction: ")
        while direction
    
