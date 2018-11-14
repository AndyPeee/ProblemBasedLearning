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
        y = 1
        for y in range (2,num):
            if num % y == 0:
                break
        else:
            return num
def prime(n):
    y = 1
    w = 1
    while w == 1:
        if y < n:
            holder = prime_numero(num=y)
            prime_list.append(holder)
            y += y
        else:
            print(prime_list)
            break
prime(n=int(input("What number do you want? ")))