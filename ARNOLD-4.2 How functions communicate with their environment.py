"""
Select Song
The itsy bitsy spider
crawled up the water spout.
Down came the rain,
and washed the spider out.
Out came the sun,
and dried up all the rain,
and the itsy bitsy spider went up the spout again.
"""
#write the function
def song(bug, adjective1, noun1, noun2, adjective2, noun3, adjective3):
    print("/n/n")
    print(f"The itsy bitsy {bug}")
    print(f"{adjective1} up the {noun1} spout.")
    print(f"Down came the {noun2},")
    print(f"and {adjective2} the {bug} out.")
    print(f"Out came the {noun3},")
    print(f"and dried up all the {noun2},")
    print(f"and the itsy bitsy {bug} {adjective3} up the spout again.")
#identify variables and collect user input
input_bug = input("Enter a type of bug:  ") #spider
input_adjective1 = input("Enter an adjective:  ")#crawled
input_noun1 = input("Enter a noun:  ")#water
input_noun2 = input("Enter another noun:  ")#rain
input_adjective2 = input("Enter another adjective:  ")#washed
input_noun3 = input("Enter another noun:  ")#sun
input_adjective3 = input("Enter another adjective:  ")#went
#call the function
song(bug=input_bug, adjective1=input_adjective1, noun1=input_noun1, noun2=input_noun2, adjective2=input_adjective2, noun3=input_noun3, adjective3=input_adjective3 )
