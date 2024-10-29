# Madison Legere, 10/28/2024, Module 2.2

# This program uses a function to convert
# miles to kilometers

def miles_to_kilometers(miles):
	"""Convert miles to kilometers."""
	return miles * 1.60934

def main():
	while True:
		try:
			# Prompt the user for input
			miles = input("Please enter the number of miles driven: ")
			# Validate input
			miles = float(miles) # Attempt to convert to float
			
			if miles < 0:
				print("Please enter a non-negative number.")
				continue
				
			# Call the conversion function
			kilometers = miles_to_kilometers(miles)
			
			# Display the results
			print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")
			break # Exit the loop if the input is valid
			
		except ValueError:
			print("Invalid input. Please enter a numeric value.")
			
if __name__ == "__main__":
	main()
