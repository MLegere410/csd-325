# Madison Legere, 11/3/2024, Module 3.2

# This program modifies the chohan program

# Introduction to the game
print("Welcome to the Chohan Game!")
print("Notice: If you roll a 2 or a 7, you get a 10 mon bonus!")

# Initialize variables
purse = 100  # Starting amount
house_percentage = 12  # Change house percentage to 12%

# Input from user with initials
roll = int(input("Enter your roll (your initials): "))

# Check for bonus
if roll == 2 or roll == 7:
    print(f"You rolled a {roll} and get a 10 mon bonus!")
    purse += 10  # Add bonus to purse

# Example calculation for house percentage (assuming some game logic here)
house_amount = (roll * house_percentage) / 100
purse -= house_amount  # Deduct house percentage from purse

# Display results
print(f"Your final purse amount is: {purse} mon")
