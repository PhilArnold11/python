# Define time slots
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# empty heart rate list
heart_rates = []

# User Input for Heart Rate
for time_slot in time_slots:
    heart_rate = int(input(f"Enter your heart rate in the {time_slot}: "))
    heart_rates.append([time_slot, heart_rate])#storing heart rate data

total = 0 #accumulator
for heart_rate in heart_rates:
    total += heart_rate[1]
#calculate average heart rate
average = round(total / len(time_slots))
print('Daily Average Heart Rate: ', average)
