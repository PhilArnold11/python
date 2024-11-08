#create a list named days that includes all seven days of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#create an empty steps list
steps=[]
#input steps
for day in days:
    steps_taken = int(input(f"How many steps did you take on {day}? "))
#store steps
    steps.append(steps_taken)
#display daily steps
for i in range(len(days)):
    print(f"You took {steps[i]} steps on {days[i]}")
#calculate total steps
total_steps = sum(steps)
print("\nTotal steps:", total_steps)
#Average steps
average = round(total_steps / len(steps))
print("Average steps:", average)