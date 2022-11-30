# Python is case sensitive!!!

# VARIABLES
# Variable names tend to be lower case and separated by underscores
string_example = 'august'
numbe_example = 100
boolean_example = True # needs to be capitalized

# STRINGS
# we can use f before strings to format them instead
# of using concatenation. It's also possible to
# use what we would call template literals in JS

name = 'Tiddles'
animal = 'cat'
temperament = 'spicy'

# same strign two different ways
unformatted_string = 'Tiddles is a ' + animal + ' who has a ' + temperament + ' temperament'
formatted_string = f'Tiddles is a {animal} who has a {temperament} temperament'
print(unformatted_string)
print(formatted_string)

# IF STATEMENTS
# For loops and if statements need lines to be terminated with colons for indentation
temperature = 13
if temperature > 10 and temperature < 20:
    print("Take a light jacket")
elif temperature >= 20:
    print("T-shirt weather")
elif temperature < 10:
    print('You need a big coat!')
print("done")

age = 17

message = "Allowed to vote" if age >= 18 else "Not allowed to vote"

print(message)

# OPERATORS
# operaotrs can be used as strings instead of &, | and !
# === is is in Python
age = 30
location = 'UK'

age and location
location = "UK" or "USA"
student = True
unemployed = True
name = "Takaya"

if age > 16 and location is "UK":
    print("You're eligible to apply")

if location is "UK" or "USA":
    print("You probably can speak English")

if not student: # this is like the bang operator, if student is false
    print("You must be a student to get discount")

if name != "Takaya":
    print("Who are you?")

if(student or unemployed) and location != "USA":
    print("You can apply for financial help!")

# is vs == matters more for objects where
# == is for value equality
# is is for reference equality

# FOR  LOOPS
# range is built in to define how many times a loop
# runs. The arguments are start point, stop point, 
# and steps to increment by
for number in range(1, 10, 2):
    print('hi', number, (number +1) * ".")

# LISTS
# unlike arrays, lists are built into Python
letters = ["a", "z", "i"]
nested_list = [[0,1 ], [2, 3]] #matrix
create_list_of_fives = [5] * 10
print(create_list_of_fives)
twenty = list(range(21)) #create a list 0-20
print(twenty)
print(len(twenty))
print(letters[1])
print(twenty[0:3])
print(twenty[::2]) # print every other number

# list unpacking ( like array destructuring )
# left side should match length of list  or error will occur
# first, second, third = twenty << error

first, second, *other = twenty # packs the remaining numbers into an list called other
print(first)
print(other)

# OBJECTS

# FUNCTIONS
# keyword to define a function is 'def'
def printMyName():
    print('august')
#call the function
printMyName()

def printAnyName(name):
    print(name)
printAnyName('Zack 🐈‍⬛')

# default values can be passed in like so
def printAnyNameOrMine(name='August'):
    print(name)
printAnyNameOrMine() # prints August
printAnyNameOrMine('Zack 🐈‍⬛') # prints Zack 🐈‍⬛

# ARRAYS