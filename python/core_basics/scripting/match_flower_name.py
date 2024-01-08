"""
Question: 
Create a function that opens the flowers.txt, 
reads every line in it, and saves it as a dictionary. 

The main (separate) function should take user input (user's first name and last name) 
and parse the user input to identify the first letter of the first name. 
It should then use it to print the flower name with the same first letter 
(from dictionary created in the first function).
"""

# Write your code here
flowers = {}
# HINT: create a dictionary from flowers.txt
def get_flowers(filename):
    with open(filename) as f:
        lines = f.readlines()
        #print(lines)
        for line in lines:
             curr_line = line.strip().split(": ")
             #print(curr_line)
             flowers[curr_line[0]] = curr_line[1]

# HINT: create a function to ask for user's first and last name
def get_name():
    name = input("Please enter your First and Last name:")
    print(flowers.get(name[0].upper(),"Sorry - we dont have a matching flower"))

# print the desired output
get_flowers("flowers.txt")
#print(flowers)
get_name()