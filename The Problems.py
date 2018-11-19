import random
#6
# Write a program that will keep track of a shopping list.
# The program will continuously ask the user for information until the user indicates completion.
# At the end, print out the shopping list.

shoppinglist = []


def shopping():
    y = 1
    while y == 1: # this loop repeatedly asks the user if they would like to continue adding to the shopping list
        stoporstart = input("Would you like to stop? ")
        if stoporstart == "yes":
            print(shoppinglist)
            return shoppinglist
        else:
            x = 1
            while x == 1: # loop to add the given item to the list
                addtolist = input("What would you like to add to the list? ")
                shoppinglist.append(addtolist)
                x = 2


shopping()
#7 Write a function that will return a list all of the prime numbers up to and including the parameter n,
# where n is an positive integer.
prime_list = []
def prime_numero(num): # function to determine if a number is prime
    if num >= 1:
        for w in range(2, num): # tries every number and runs it through a loop
            if num % w == 0: # finds out if number is prime by looking for a remainder (if there is it's prime)
                break
        else:
            return num
    return ""
def prime(n):
    y = 2
    w = 1
    while w == 1:
        if y <= n:
            holder = prime_numero(y) # inputs a number into the function to check for a prime number
            prime_list.append(holder)
            y += 1 # changes the number being tested if it is prime or not
        else:
            print(prime_list) #finishes the loop when the input number is reached
            break


prime(int(input("What number do you want? "))) # takes the number in to find all the prime numbers up to it

#Write a program that will keep track of a simulated dice being rolled a given number of times (by the user).
# The program should print the number of times each result was rolled.
dicelist = []
def sum_of_dice(dice, numrolls):
    amount = 0
    for x in range(0, int(numrolls)):
        amount = random.randint(1, dice) # "rolls" the dice
        dicelist.append(amount) # adds the number rolled to the end of the list
    print(dicelist)
    print((dicelist.count(1)), " ones") # counts the amount of each number, and prints it to the console
    print((dicelist.count(2)), " two's")
    print((dicelist.count(3)), " three's")
    print((dicelist.count(4)), " fours")
    print((dicelist.count(5)), " five's")
    print((dicelist.count(6)), " sixes")


sum_of_dice(dice=6, numrolls=int(input("How many times do you want to roll this dice? ")))

#Write a function called pivotList(inList, number)
# that will return a list composed of all elements from inList that are less than number.
# inList is a list of numbers, and number is the pivot value.

listy = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
listy2 = []
def pivotlist(inlist, number):
    g = 1
    for g in range(len(listy)): # checks every number in the list if it is less than number
        if number > inlist[g]:
            listy2.append(inlist[g]) # if the list value is less than the number, it adds it to the end of the new list
    print(listy2) # prints the new list made


pivotlist(inlist=listy, number=int(input("What number do you want? "))) # intakes the value for the "pivot"

#Write a function called largestValue(inList) that will return the largest value in the inList of numbers.
# (You may not use the ‘max’ feature of lists to write this function)
hugelist = [0, 1, 2, 1000000000, 4, 5, 7, 6, 4, 8]
def largest_value(big_list): # function sorts the list, so the larges value is last
    big_list.sort()
    print(big_list[(len(big_list)-1)]) # takes the last item in the list and prints it
largest_value(big_list=hugelist)

#Write a function called mergeList(list1, list2) that will take two lists (list1 and list2,
# both of which are sorted) as parameters and will return a single list that merges the two lists together into a single sorted list.
# You may not use the .sort() function available to lists.

list1 = [5, 1, 9, 8, 4]
list2 = [0, 6, 2, 3, 7]


def mergelist(merge1, merge2):
    for e in range(0, len(merge2)): # takes the length of the second list, and repeats the loop that many times
        f = merge2[e] # takes the index in the loop, and puts it in the loop
        merge1.append(f)
        bubblesort(merge1) # puts the new list into a sorting function
    print(merge1)


def bubblesort(merge1):
    for passthenum in range(len(merge1)-1, 0, -1): # checks the value being sorted in the loop against every other number in the loop
        for i in range(passthenum):
            if merge1[i] > merge1[i+1]: # if the value is larger than the next it gets moved to where it should be
                holder1 = merge1[i]
                merge1[i] = merge1[i+1]
                merge1[i+1] = holder1


mergelist(merge1=list1, merge2=list2)

#There is a four player game that involves rolling a dice for each player.
# Write a program that will keep track of the history of the rolls for each player.
# For full credit, how could you use 2D lists?
dice = 6
biglist = [[], [], [], []] # makes the list to be appended into
for x in range(4): # range of 4 for the 4 players
    g = int(input("amount of times to roll ")) # takes in the input of how many times each player wants to roll
    for y in range(g):
        dice_value = random.randint(1, dice) #"rolls" the dice
        biglist[x].append(dice_value) # appends the roll into the position on the 2d list
print(biglist)


#Write a program that simulates Tic-Tac-Toe. For full credit, your game must make use of 2D lists.

top_row = ["tl","tm","tr"] # makes the board
middle_row = ["ml","mm","mr"]
bottom_row = ["bl","bm","br"]
board = [[top_row], [middle_row], [bottom_row]]
print(board[0]) # prints the board for the player
print(board[1])
print(board[2])
def tictactoe(move, q):
    if move == "tl": # takes in a coordinate and changes the value accordingly
        if q % 2 == 0: # determines which player is making their move
            top_row[0] = "X"
        else:
            top_row[0] = "O"
    elif move == "tm":
        if q % 2 == 0:
            top_row[1] = "X"
        else:
            top_row[1] = "O"
    elif move == "tr":
        if q % 2 == 0:
            top_row[2] = "X"
        else:
            top_row[2] = "O"
    elif move == "ml":
        if q % 2 == 0:
            middle_row[0] = "X"
        else:
            middle_row[0] = "O"
    elif move == "mm":
        if q % 2 == 0:
            middle_row[1] = "X"
        else:
            middle_row[1] = "O"
    elif move == "mr":
        if q % 2 == 0:
            middle_row[2] = "X"
        else:
            middle_row[2] = "O"
    elif move == "bl":
        if q % 2 == 0:
            bottom_row[0] = "X"
        else:
            bottom_row[0] = "O"
    elif move == "bm":
        if q % 2 == 0:
            bottom_row[1] = "X"
        else:
            bottom_row[1] = "O"
    elif move == "br":
        if q % 2 == 0:
            bottom_row[2] = "X"
        else:
            bottom_row[2] = "O"
    print(board[0]) # prints the board after the turn has been done
    print(board[1])
    print(board[2])
    did_i_win() # runs a function to determine if you won or not


def did_i_win():
    if top_row[0] == middle_row[0] and middle_row[0] == bottom_row[0]: # runs through every possible winning layout, and ends the game if any of them are true
        return "win"
    elif top_row[1] == middle_row[1] and middle_row[1] == bottom_row[1]:
        return "win"
    elif top_row[2] == middle_row[2] and middle_row[2] == bottom_row[2]:
        return "win"
    elif top_row[0] == top_row[1] and top_row[1] == top_row[2]:
        return "win"
    elif middle_row[0] == middle_row[1] and middle_row[1] == middle_row[2]:
        return "win"
    elif bottom_row[1] == bottom_row[0] and bottom_row[0] == bottom_row[2]:
        return "win"
    elif top_row[0] == middle_row[1] and middle_row[1] == bottom_row[2]:
        return "win"
    elif top_row[2] == middle_row[1] and middle_row[1] == bottom_row[0]:
        return "win"


q = 0
while did_i_win() != "win":
    tictactoe(input("What move do you want to make? "), q)
    q += 1
    if q == 9: # if all the squares (9) are filled, and no one won, the game is a tie
        print("It's a tie!")
        break
if did_i_win() == "win":
    print("You win")
