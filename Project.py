#------------------------------------------------------------------------------------------
#
# Title: LDE/Modulo_EQ Calculator
# Creator: Ashish Tamang
# Student of University of Waterloo
# Created: Winter 2014
#
# Synopsis:
#          
#          A text-based Dungeon Crawling RPG made in Python. It employs the use of
#          Object Oriented Programming to handle stats of the characters and monsters.
#          Careful attention has been paid to balancing the game to make the playing
#          experience as pleasurable as possible.
#
# Description:
#
#          In BLT_RPG, you are an adventure raiding a floating castle inhabited by 
#          the notorious bandit guild, 'Neko Hooligans'. In the character creation section, 
#          you must pick one of five classes: 
#          
#               i) Berserker ii) Hemomancer iii) Weaponmaster iv) Archmage v) Lone Wolf
#          
#          With a weapon in hand, your objective is cleave through the Hooligans, ascend
#          the three floors of the floating castle and confront the ever-elusive 
#          phantom leader of the guild.
#
#
# Instructions:
#
#          The game is very easy to play. It is text-based and therefore every interaction,
#          --whether it is traversing through the dungeon, fighting monsters 
#          or checking one's stats-- is done through the use of I/O with Python. 
#
#
# Possible Future Updates:
#
#          i) Cleaner Battles; easier to distinguish damage
#         ii) The integration of a map to make traversing a bit easier
#        iii) The introduction of a GUI
#
#
#-------------------------------------------------------------------------------------------
import math
from fractions import gcd

def LDE_check():
    print("\nWe will be solving for all the values of x and y in the form: 'ax + by = c'\n")
    while True:     
        a = input("What would you like your 'a' to be? --> ")
        try:
            a = int(a)
            if a == 0:
                print ("'a' or 'b' cannot be zero!")
            else:
                break
        except ValueError:
            print("Please enter a valid input.\n")
    while True:
        b = input("What will be your 'b'? --> ")
        try:
            b = int(b)
            if b == 0:
                print ("'a' or 'b' cannot be zero!")
            else:
                break
        except ValueError:
            print("Please enter a valid input.\n")
    while True:
        c = input("Lastly, what is your 'c'? --> ")
        try:
            c = int(c)
            break
        except ValueError:
            print("Please enter a valid input.\n")
    d = gcd(a,b)
    quotient = c/d
    print ("\nThe GCD of", a, "and", b, "is", str(d)+".")
    if not(quotient.is_integer()):
        return "There are no integer solutions in x and y for this particular set of input."
    elif c == 0:
        return Zero_Route(a,b, d)
    else:
        return LDE_Solve(a, b, c, d)


def LDE_Solve(a, b, c, d):
    x, y = Initialize(a, b)
    x, y = str(int(x * c/d)), str(int(y * c/d))
    first, second = str(int(b/d)), str(int(-a/d))
    Answer = "The complete solution in LDE is... "+"\n  x = "+x+" + ("+first+")n \n  y = "+y+" + ("+second+")n \nwhere n can be any integer!"
    return Answer


def Zero_Route(a,b,d):
    first = str(int(b/d))
    second = str(int(-a/d))
    Answer = "The complete solution in LDE is... "+"\n  x = ("+first+")n \n  y = ("+second+")n \nwhere n can be any integer!"
    return Answer


def MOD_check():
    print ("\nWe will be solving for all the values of x in the form: 'ax ≡ b (mod m)'\n")
    while True:
        a = (input("What would you like your 'a' to be? --> "))
        try:
            a = int(a)
            if a == 0:
                print ("'a' cannot be zero!")
            else:
                break
        except ValueError:
            print("Please enter a valid input.\n")
    while True:      
        b = (input("What will be your 'b'? --> "))
        try:
            b = int(b)
            break
        except ValueError:
            print("Please enter a valid input.\n")
    while True:
        mod = input("Lastly, what is the modulus? --> ")
        try:
            mod = int(mod)
            if mod > 0:
                break
            else:
                print("Please enter a valid modulus!\n")
        except ValueError:
            print("Please enter a valid input.\n")
    d = gcd(a,b)
    quotient = mod/d
    print (quotient)
    print ("\nThe GCD of", a, "and", b, "is", str(d)+".")
    if mod == 1:
        return "The solution in Modulo notation is... "+"\n  x = 0 (mod 1)"
    elif a == 1:
        return One_a(b, mod)
    elif quotient.is_integer():
        return MOD_Solve(a, b, mod, d)
    else:
        return "There are no integer solutions in x and y for this particular set of input."


def MOD_Solve(a, b, mod, d):
    x, y = Initialize(a, mod)
    x = int(x * b/d)
    if x < mod:
        while True:
            x = x + mod
            if x > 0:
                break
    elif x >= mod:
        while True:
            x = x - mod
            if x < mod:
                break
    x,mod = str(x), str(mod)
    Answer = "The complete solution in Modulo notation is... "+"\n  x = "+x+" (mod "+mod+")"
    return Answer


def One_a(b, mod):
    if b < mod:
        while True:
            b = b + mod
            if b > 0:
                break
    elif b >= mod:
        while True:
            b = b - mod
            if b < mod:
                break
    b,mod = str(b), str(mod)
    Answer = "The complete solution in Modulo notation is... "+"\n  x = "+b+" (mod "+mod+")"
    return Answer
    
def Initialize (a, b):
    if a >= b:
        return EEA_Algorithm (a, b, 1, 0, 0, 1)
    else:
        return EEA_Algorithm (b, a, 0, 1, 1, 0)


def EEA_Algorithm(a, b, i_x, i_y, ii_x, ii_y):
    n = b
    while True:
        quotient = math.floor(a/b)
        new_n = a - b * quotient
        if new_n == 0:
            return ii_x, ii_y
        else:
            i_x, ii_x = Calculate_XY (i_x, ii_x, quotient)
            i_y, ii_y = Calculate_XY (i_y, ii_y, quotient)
            store_n, a, b = new_n, b, new_n

            
def Calculate_XY(i, ii, quotient):
    new_ii = ii * quotient
    holder = i - new_ii
    i, ii = new_ii, holder
    return i, ii


#main

print ("\nWelcome to LDE/Modulo Equation Calculator!")

while True:
    while True:
        Choice = input("\nWhat would you like solved?\n  1) Linear Diophantine Equation\n  2) Modulus Equation\n--> ")
        if Choice == "1":
            print(LDE_check())
            break
        elif Choice == "2":
            print(MOD_check())
            break
        else:
            print ("\nPlease enter a valid entry - ('1' or '2').")
    Choice_2 = input("\nWould you like to perform another action?\n  1) Yes, of course.\n  2) No, thank you.\n--> ")
    if Choice_2 == "2":
        print ("\nThank you for using MATH135_Helper.\nSee you next time!")
        break
