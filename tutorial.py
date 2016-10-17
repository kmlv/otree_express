# Single line comments start with a number symbol.
""" Multiline strings can be written
    using three "s, and are often used
    as comments
"""

####################################################
## 1. Primitive Datatypes and Operators
####################################################

# you hav numbers

# math is what you would expect
88/13
# enforce precedence with parenthesis
(1+3)*2
# boolean
True
False
True and True
True or False
True and False
not True
True == False
'a' == 'a'
2 == 2
2 != 2

# chain cof compatrisons
1 < 3 < 2
1 < 3 < 4

# " or '
"a"
'a'

# addition of strings
'que tal' + ' ...'

# strings are LISTS of Characters ##
'abcde'[0]
'abcde'[2]

# FORMAT method: fills out placeholders ##
"{} is a {}".format("this", "placeholder")

"{} is a {}".format("this", "placeholder")

# None
None

### bool
bool(0)
bool(None)
bool('')

"""
    variables
"""

# print

print("hello there")

#declare and assign in one statement ##

myvar = 4
myvar

myvar += 1
myvar

# lists store sequences

my_list = []
my_list

other_list = [1, 3, 4]
other_list[0]

# append stuff to lists ##
my_list.append(2)
my_list

# assign value to list entry ##
other_list[2] = 8
other_list

# list indices go from -n to n-1 ##
my_list[-1]

# within list ranges
# it is a closed / open range
my_list = my_list + other_list
my_list[0:2]

my_list[0:] == my_list # true

# existence in list

'a' in my_list

# length of a list
len(my_list)

# dictionaries are indexed lists
empty_dict = {}

filled_dict = {"one": 1, "two": 2}

filled_dict["one"]

filled_dict["one___"]

# only keys are searchable in dicts
"one" in filled_dict


################
# control flow
################

some_var = 10

if some_var > 10:
    print("some var is bigger than 10.")
elif some_var < 10:
    print("some_var is smaller than 10.")
else:
    print("some_var is 10")

# loops that iterate over lists  ###
for element in ['"a"', 'b', 'c']:
    print("{} is an element".format(element))

# range size n starting in zero: from [0] to [n-1]
for i in range(6):
    print(i)

# same as:
for i in range(0, 6):
    print(i)
# that is, it is a close / open range of [0, 1, 2, ...]


#######################
# functions
#######################

def add(x, y):
    print("we add {} and {}".format(x, y))
    return x + y

add("e", "t")
add(4, 5)
add(x=5, y=6)

# list comprenhensions  ###

[add(i, 4) for i in [1, 6, 18]]

[x for x in [1, 2, 3, 4, 5, 6] if x >3]

#####################
# MODULES
"""
    Python modules are just ordinary python files. You
    can write your own, and import them. The name of the
    module is the same as the name of the file.
"""
#####################

import random
import math

print(math.sqrt(16))

from math import ceil, floor

print(ceil(3.7))

print(floor(3.7))





###################
# CLASSES
###################

# classes let you model real life entities

# class allows to subclass object (everything is an object)

class Mammal(object):

    # a class attribute
    classification = "Mammalia"

    classification2 = "Organism"

    # methods are functions that belong to a class ###
    # all methods take self as first argument
    # method called set_age sets age of an individual mammal
    def set_age(self):  # this defines the method
        self.age = 0    # notice it is ".age"

    def older_than_10(self):
        return self.age > 10

    # method with arguments
    def predict_age(self, years):
        return 'In {} years I will be {}'.format(years, self.age + years)

class Dog(Mammal): # is subclassing Mammal
    classification = "Canis Lupus"

    def bark(self):
        return "woof"



Mammal.classification
Mammal.classification2

Dog.classification
Dog.classification2

# Instantiating classes
lassie = Dog()  # applying method
lassie.classification
lassie.classification2

lassie.bark()

lassie.set_age()

lassie.age # calling value

lassie.older_than_10()

lassie.age = 11

lassie.older_than_10()





















#############################################################
##              original notes
#############################################################

# google learn x in y minutes for x=python



# Single line comments start with a number symbol.

""" Multiline strings can be written
    using three "s, and are often used
    as comments
"""

####################################################
## 1. Primitive Datatypes and Operators
####################################################

# You have numbers
from numpy.core.defchararray import array

3  # => 3

# Math is what you would expect
1 + 1  # => 2
8 - 1  # => 7
10 * 2  # => 20
35 / 5  # => 7

# Enforce precedence with parentheses
(1 + 3) * 2  # => 8

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False  # => False
False or True  # => True

# negate with not
not True  # => False
not False  # => True

# Equality is ==
1 == 1  # => True
2 == 1  # => False

# Inequality is !=
1 != 1  # => False
2 != 1  # => True

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Comparisons can be chained!
1 < 2 < 3  # => True                            ###
2 < 3 < 2  # => False

# Strings are created with " or '
"This is a string."
'This is also a string.'

# Strings can be added too!
"Hello " + "world!"  # => "Hello world!"        ###

# A string can be treated like a list of characters
"This is a string"[0]  # => 'T'   ###

# format strings with the format method.        ###
"{} is a {}".format("This", "placeholder")  ###

# None is an object
None  # => None

# Any object can be used in a Boolean context.  ###
# The following values are considered falsey:
#    - None
#    - zero of any numeric type (e.g., 0, 0L, 0.0, 0j)
#    - empty sequences (e.g., '', [])
#    - empty containers (e.g., {})
# All other values are truthy (using the bool() function on them returns True).
bool(0)  # => False                             ###
bool("")  # => False

####################################################
## 2. Variables and Collections
####################################################

# Python has a print statement
print("I'm Python. Nice to meet you!")  # => I'm Python. Nice to meet you!

# No need to declare variables before assigning to them.
some_var = 5  # Convention is to use lower_case_with_underscores
some_var  # => 5

# incrementing and decrementing a variable
x = 0
x += 1  # Shorthand for x = x + 1               ###
x -= 2  # Shorthand for x = x - 2               ###

# Lists store sequences
li = []
# You can start with a prefilled list
other_li = [4, 5, 6]

# Add stuff to the end of a list with append
li.append(1)  # li is now [1]
li.append(2)  # li is now [1, 2]              ###
li.append(3)  # li is now [1, 2, 3]

# Access a list like you would any array
li[0]  # => 1                                   ### lists start in index 0
# Assign new values to indexes that have already been initialized with =
li[0] = 42
li[0]  # => 42
li[0] = 1  # Note: setting it back to the original value
# Look at the last element
li[-1]  # => 3                                  ###

# You can look at ranges with slice syntax.
# (It's a closed/open range.)                   ### ### ### ###
other_li[1:2]  # => [5, 6]                      ###
# Omit the beginning
other_li[1:]  # => [5, 6]
# Omit the end
other_li[:2]  # => [4, 5]

# You can add lists
li + other_li  # => [1, 2, 3, 4, 5, 6]         ###
# Note: values for li and for other_li are not modified.

# Check for existence in a list with "in"
1 in li  # => True                             ###

# Examine the length with "len()"
len(li)  # => 6

# Dictionaries store mappings
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}  ###

# Look up values with []
filled_dict["one"]  # => 1

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict  # => True
1 in filled_dict  # => False

# Looking up a non-existing key is a KeyError
# filled_dict["four"]   # raises KeyError!

# set the value of a key with a syntax similar to lists
filled_dict["four"] = 4  # now, filled_dict["four"] => 4   ###

####################################################
## 3. Control Flow
####################################################

# Let's just make a variable
some_var = 5

# Here is an if statement.
# prints "some_var is smaller than 10"
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:  # This elif clause is optional.
    print("some_var is smaller than 10.")
else:  # This is optional too.
    print("some_var is indeed 10.")

"""
SPECIAL NOTE ABOUT INDENTING
In Python, you must indent your code correctly, or it will not work.
(Python is different from some other languages in this regard)
All lines in a block of code must be aligned along the left edge
When starting a code block (e.g. "if", "for", "def"; see below), you should indent by 4 spaces.
When ending a code block, you should unindent by 4 spaces.

Examples of improperly indented code:

if some_var > 10:
print("bigger than 10." # error, this line needs to be indented by 4 spaces


if some_var > 10:
    print("bigger than 10.")
 else: # error, this line needs to be unindented by 1 space
    print("less than 10")

"""

"""
For loops iterate over lists
prints:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # You can use {} to interpolate formatted strings. (See above.)
    print("{} is a mammal".format(animal))

"""
"range(number)" returns a list of numbers
from zero to the given number
prints:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(lower, upper)" returns a list of numbers
from the lower number to the upper number
prints:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)


####################################################
## 4. Functions
####################################################

# Use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement


# Calling functions with parameters
add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11

# Another way to call functions is with keyword arguments
add(y=6, x=5)  # Keyword arguments can arrive in any order.

# We can use list comprehensions to loop or filter
[add(i, 10) for i in [1, 2, 3]]  # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]
array()
####################################################
## 5. Modules
####################################################

# You can import modules
import math

print(math.sqrt(16))  # => 4

# You can get specific functions from a module
from math import ceil, floor

print(ceil(3.7))  # => 4.0
print(floor(3.7))  # => 3.0


# Python modules are just ordinary python files. You
# can write your own, and import them. The name of the
# module is the same as the name of the file.

####################################################
## 6. Classes
####################################################

# classes let you model complex real-world entities

class Mammal(object):
    # A class attribute. It is shared by all instances of this class
    classification = "Mammalia"

    # A method called "set_age" that sets the age of an individual mammal
    # Methods are basically functions that belong to a class.
    # All methods take "self" as the first argument
    def set_age(self):  ### this generates the attribute age
        self.age = 0

    # method that returns True or False
    def older_than_10(self):
        return self.age > 10

    # method with argument
    def predict_age(self, years):
        return 'In {} years I will be {}'.format(years, self.age + years)


class Dog(Mammal):
    classification = "Canis lupus"

    def bark(self):
        return "woof!"


Mammal.classification

# Instantiate a class
lassie = Dog()
lassie.classification  # => "Canis lupus"
lassie.set_age()  ### this generates the attribute age
lassie.older_than_10()  # => False
lassie.age = 11
lassie.older_than_10()  # => True
lassie.bark()  # => "woof!"


###############################################################


class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs)

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)

        container.pack(side="top", fill="top", expand="True")


#############################################################
# old note from 2.*

output = 'reagant : %d' % 123
print
output

output = 'reagant : %6.2f' % 12.3
print
output

# formatting more than one
var1 = 123
var2 = 12.5
print
'text1 %d text2 %6.2f%% text3' % \
(var1, var2)

# \ backslash breaks lines


print



''  #####################################
# some formatting characters: \n  \\  \'  \"

print
'this line ends here\n and quoting someone\n\
\"this is the new line\'s end\"'

print
''' this line 1
line 2
line 3 only using three quotes'''

#
print
'#####################################'
print
'# some methods for strings'

strvar = 'KRIstian'
print
strvar.capitalize()
print
strvar.lower()
print
strvar.upper()

print
'#####################################'
print
'# some methods for strings'

strvar = 'KRIstian'
print
strvar.count('i') ## search for occurences of 'i'

print
strvar.lower().count('i')

strvar2 = "abcsa"

strvar2.count("a")


print
'#####################################'
print
'ALIASING'

string1 = 'isaac'
string2 = string1
print
string1
print
string2
# BUT IF string1 changes...
# string2 does not change
string1 = string1 + ' newton'
print
string1
print
string2

# HOWEVER LIST ARE MUTABLE ##############!!!
# string2 does not change
list1 = ['isaac']
list2 = list1

list1

list2

list1 = ['isaac']
list1
list1.append('Newton')

list1

list2

#################################
print
'##################'


def greet():
    return 'Hey!'


print
greet()


def greet(name):
    return 'Hey! ' + name


print
greet('KL')

str_var = greet('You!')
str_var

print
'-------------------------------'


## STACKS FRAMES RELATES TO THE SCOPE WHICH VARS ARE USED

def fun(arg):
    Loc1 = 'fun add: ' + arg
    return Loc1


fun("a")

str_var = 'values'

result


# locals of current frame are discarded when a function return



# Every function returns something.
# If nothing is defined then returns "none"

def appender(str_, list_):
    str_ += 'turing'
    list_.append('turing')


str_val = 'alan'
list_val = ['alan']
appender(str_val, list_val)

str_val
list_val

list_val2 = ['alan']
list_val2.append('turing')

list_val2

# this was the previous problem
list1 = ['isaac']
list1.append('Newton')
list1



####################################################
# functions with default values'


#  OJO: defaulted args must come later!!

def adjust(value, amount=2):
    return value * amount


print
adjust(5)
# outs 10
print
adjust(5, 22)
# outs 110

# when should we write fn?
# Humans can hold 7 objects top
# keep same level of calling variables and doing clear processing to those variables
# to go into a deeper levels CREATE Functions
# Typical "good programmer" would:
# 1) write top level
# 2) write second level functions
# 3) so on
# 4) reassign overlaps


####################################################
print
'==========================='
print
'First Class Functions'
print
'functions are just data'


# example ##  see the call of sum is expecting a list arg [1, 2, 4]
def funcione(var):
    return 1.0 / sum(var)  # will give one decimal

a = [3, 4]
funcione(a)

sum([])

t = funcione
print
t([1, 2, 3, 4])

# you can loop inside a function

PI = 2.1416


def area(r):
    return PI * r * r


def circ(r):
    return PI * 3 * r


area(20)
circ(1)


# # you can do functions of functions!!!
# # AKA: higher order function
# # notice the call for function "fun"!

def callit(fun, val):
    return fun(val)  ###

print
callit(area, 1)

# # looping over a list of functions!

funcsss = [area, circ]

for ff in funcsss:
    ff(1.3)

# # BTW this is invalid:
funcsss


# # MORE
def do_all(fun, vals):
    result = []
    for v in vals:
        temp = fun(v)
        result.append(temp)
    return result

# #
do_all(area, [3, 5.1, 7.1])


#### COMBINING VALUES WITH AND ABSTRACT FUNCTION
#
def combine_values(func, values):
    current = values[0]
    for i in range(1, len(values)):
        current = func(current, values[i])  ## ERROR IN NOTES: [i]?
    return current


def add(x, y): return x + y


combine_values(add, [3, 5, 10])


# higuer order functions let us do more with less code
# in python number of args not very important

# another version of combine but with TUPLES
def combine_values2(func, *values):
    current = values[0]
    for i in range(1, len(values)):
        current = func(current, values[i])
    return current


def add(x, y): return x + y

combine_values2(add, 3, 5, 10)  # no need of list notation

combine_values2(add, 1, 2)

add(2, 3)


## IMPORTANT HIGHER ORDER FUNCTONS

# FILTER
def posit(x): return x >= 0


list(filter(posit, [-1, -2, 0, 5]))  ### returns [0, 5]

list(map(posit, [-1, -2, 0, 5]))   ### returns [False, False, True, True]



############################################
# SLICING!
print
'SLICE!'

# look at this difference

original_list1 = [1, 2, 3, 4, 5]

middle_list1 = original_list1[2:-1]

original_list1
middle_list1

middle_list1[0] = 'a'
middle_list1[1] = 'b'

original_list1
middle_list1

#############
'example 2'

original_list = [[1, 1], [2, 1], [3, 3], [4, 1], [5, 3]]

middle_list = original_list[2:-1]

original_list
middle_list

middle_list[0][1] = 'a' ###
middle_list[1][1] = 'b' ###


original_list  #### this one also changes!!

middle_list


#############
'example 3'

original_list = [[1], [2], [3], [4], [5]]
middle_list = original_list[2:-1]

original_list
middle_list

middle_list[0][0] = 'a'
middle_list[1][0] = 'b'

original_list
middle_list

# suppose you have a list of lists, and take a subset of lists and modify them
# Because you point entire lists inside a list and modify those (#####)
# then you also modify those lists inside the original list of lists (ex 2 & 3)
# but if the original is a simple list each entry is not a list and therefore is
# not mutable (this is example 1)


# ==========================


"Ola" * 3

"Runnin' down the hill"

'Runnin\' down the hill'

"Ola".upper()

'Ola'.pop(0)
