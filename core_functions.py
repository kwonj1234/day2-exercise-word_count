#exercise 1

#print()
# Print a text stream into the terminal of 1 or more objects.
statement = "I don't feel so good Mr.Stark"
print(statement,"-","Spiderman")

#input()
#Prompts the user to input a string which the input() function
#returns.
x = int(input("Give me a number: "))
print("This is 10 more than that number, ", x+10)

# .is methods
# .is methods identify properties of elements in strings 
# and return True or False values.
print(statement.isalpha())
print(statement.isalnum())
print(statement.isspace())
print(statement.islower())

#round()
#Rounds a number to a precision of 'n' digits. If 'n' 
#is not specified, it rounds to the nearest integer.
print(round(3.7665432,3))
print(round(0.5)) #If two numbers are equally close, 
                  #round() always round to the even

#len()
#Returns the number of items in an object.
print(len(statement))
print(len([1,2,3,4,5,6]))
print(len(["Hello","World"]))

#sum()
#Sums a list of int values from some begining value x,
#If no beginning value is specified, it's 0 by default
sum([1,2,3,4],100)

#type functions
#int() and string() can create or convert int and 
#string type objects from one to the other, while 
#dict() only creates dictionaries and tuple()
#only creates tuples
int("56")
str(56)
d = dict({"Spiderman":"Not Good", "Mr.Stark": "Depressed"})
tuple([42])

