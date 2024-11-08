#Accept 5 names from user and store in a list
names = []
for i in range(5):
    name = input("Enter a name: ")
    names.append(name)
#flag to track if a swap has occured
swapped=True
#make names lower case
for i in range(0, len(names)):
    names[i] = names[i].lower()
#swap until no swaps occur
while swapped:
    swapped = False 
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            swapped = True  
            names[i], names[i + 1] = names[i + 1], names[i]
#print sorted list
print(names)
# Reverse the list
names.reverse()
# Print the reversed list
print(names)