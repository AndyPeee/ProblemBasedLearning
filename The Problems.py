import random
#6
# Write a program that will keep track of a shopping list.
# The program will continuously ask the user for information until the user indicates completion.
# At the end, print out the shopping list.

shoppinglist = []


def shopping():
    y = 1
    while y == 1:
        stoporstart = input("Would you like to stop? ")
        if stoporstart == "yes":
            print(shoppinglist)
            return shoppinglist
        else:
            x = 1
            while x == 1:
                addtolist = input("What would you like to add to the list? ")
                shoppinglist.append(addtolist)
                x = 2


shopping()
#7 Write a function that will return a list all of the prime numbers up to and including the parameter n,
# where n is an positive integer.
prime_list = []
def prime_numero(num):
    if num >= 1:
        for w in range(2, num):
            if num % w == 0:
                break
        else:
            return num
    return ""
def prime(n):
    y = 2
    w = 1
    while w == 1:
        if y <= n:
            holder = prime_numero(y)
            prime_list.append(holder)
            y += 1
        else:
            print(prime_list)
            break


prime(int(input("What number do you want? ")))

#Write a program that will keep track of a simulated dice being rolled a given number of times (by the user).
# The program should print the number of times each result was rolled.
dicelist=[]
def sum_of_dice(dice, numrolls):
    amount = 0
    for x in range(0, int(numrolls)):
        amount = random.randint(1, dice)
        dicelist.append(amount)
    print(dicelist)
    print((dicelist.count(1)), " ones")
    print((dicelist.count(2))," two's")
    print((dicelist.count(3))," three's")
    print((dicelist.count(4))," fours")
    print((dicelist.count(5))," five's")
    print((dicelist.count(6))," sixes")




sum_of_dice(dice=6, numrolls=int(input("How many times do you want to roll this dice? ")))

#Write a function called pivotList(inList, number)
# that will return a list composed of all elements from inList that are less than number.
# inList is a list of numbers, and number is the pivot value.

listy = [0,1,2,3,4,5,6,7,8,9]
listy2 = []
def pivotlist(inlist, number):
    g = 1
    for g in range(len(listy)):
        if number > inlist[g]:
            listy2.append(inlist[g])
    print(listy2)


pivotlist(inlist=listy, number=int(input("What number do you want? ")))

#Write a function called largestValue(inList) that will return the largest value in the inList of numbers.
# (You may not use the ‘max’ feature of lists to write this function)
hugelist = [0,1,2,1000000000,4,5,7,6,4,8]
def largest_value(big_list):
    big_list.sort()
    print(big_list[(len(big_list)-1)])
largest_value(big_list=hugelist)

#Write a function called mergeList(list1, list2) that will take two lists (list1 and list2,
# both of which are sorted) as parameters and will return a single list that merges the two lists together into a single sorted list.
# You may not use the .sort() function available to lists.

list1 = [5, 1, 9, 8, 4]
list2 = [0, 6, 2, 3, 7]
def mergelist(merge1, merge2):
    for e in range(0, len(merge2)):
        f = merge2[e]
        merge1.append(f)
        bubblesort(merge1)
    print(merge1)

def bubblesort(merge1):
    for passthenum in range(len(merge1)-1, 0, -1):
        for i in range(passthenum):
            if merge1[i] > merge1[i+1]:
                holder1 = merge1[i]
                merge1[i] = merge1[i+1]
                merge1[i+1] = holder1


mergelist(merge1=list1, merge2=list2)

#There is a four player game that involves rolling a dice for each player.
# Write a program that will keep track of the history of the rolls for each player.
# For full credit, how could you use 2D lists?
dice = 6
biglist=[[],[],[],[]]
for x in range(4):
    g=int(input("amount of times to roll "))
    for y in range(g):
        dice_value = random.randint(1, dice)
        biglist[x].append(dice_value)
print(biglist)


#Write a program that simulates Tic-Tac-Toe. For full credit, your game must make use of 2D lists.

top_row = ["tl","tm","tr"]
middle_row = ["ml","mm","mr"]
bottom_row = ["bl","bm","br"]
print(top_row)
print(middle_row)
print(bottom_row)
def tictactoe(move,q):
    if move == "tl":
        if q%2==0:
            top_row[0]="X"
        else:
            top_row[0]="O"
    elif move == "tm":
        if q%2==0:
            top_row[1]="X"
        else:
            top_row[1]="O"
    elif move == "tr":
        if q%2==0:
            top_row[2]="X"
        else:
            top_row[2]="O"
    elif move == "ml":
        if q%2==0:
            middle_row[0]="X"
        else:
            middle_row[0]="O"
    elif move == "mm":
        if q%2==0:
            middle_row[1]="X"
        else:
            middle_row[1]="O"
    elif move == "mr":
        if q%2==0:
            middle_row[2]="X"
        else:
            middle_row[2]="O"
    elif move == "bl":
        if q%2==0:
            bottom_row[0]="X"
        else:
            bottom_row[0]="O"
    elif move == "bm":
        if q%2==0:
            bottom_row[1]="X"
        else:
            bottom_row[1]="O"
    elif move == "br":
        if q%2==0:
            bottom_row[2]="X"
        else:
            bottom_row[2]="O"
    print(top_row)
    print(middle_row)
    print(bottom_row)
    did_i_win()
def did_i_win():
    if top_row[0]==middle_row[0] and middle_row[0]==bottom_row[0]:
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


q=0
while did_i_win()!= "win":

    tictactoe(input("What move do you want to make? "), q)
    q+=1
if did_i_win()=="win":
    print("You win")