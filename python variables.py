# Define variable for kilogram values
kg_value_1 = 5
kg_value_2 = 22
kg_value_3 = 25.4
kg_value_4 = 22.2
kg_value_5 = 100

# Conversion factor: 1 kg = 2.20462
conversion_factor = 2.20462

# Calculate kilograms for each pound value
lb_value_1 = kg_value_1 / conversion_factor
lb_value_2 = kg_value_2 / conversion_factor
lb_value_3 = kg_value_3 / conversion_factor
lb_value_4 = kg_value_4 / conversion_factor
lb_value_5 = kg_value_5 / conversion_factor

# Output the results
print(f"{kg_value_1} kilograms is equal to {lb_value_1:.2f} pounds.")
print(f"{kg_value_2} kilograms is equal to {lb_value_2:.2f} pounds.")
print(f"{kg_value_3} kilograms is equal to {lb_value_3:.2f} pounds.")
print(f"{kg_value_4} kilograms is equal to {lb_value_4:.2f} pounds.")
print(f"{kg_value_5} kilograms is equal to {lb_value_5:.2f} pounds.")