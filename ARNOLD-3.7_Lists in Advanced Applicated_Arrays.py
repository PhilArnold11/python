# Define time slots
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# empty heart rate list
heart_rates = []

# User input for heart rate
for time_slot in time_slots:
    heart_rate = int(input(f"Enter your heart rate (in BPM) in the {time_slot}: "))
    heart_rates.append([time_slot, heart_rate])

# Calculate average heart rate
total_heart_rate = sum(hr[1] for hr in heart_rates)
average_heart_rate = total_heart_rate / len(heart_rates)

# Print the average heart rate
print(f"Average heart rate today: {average_heart_rate} BPM")
