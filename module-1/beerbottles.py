# Madison Legere, 10/27/2024, Module 1.3

# This program outputs the reverse counting song
# "100 bottles of beer on the wall"

def countdown(bottles):
	if bottles > 1:
		print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
		print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.\n")
		countdown(bottles - 1)
	elif bottles == 1:
		print("1 bottle of beer on the wall, 1 bottle  of beer.")
		print("Take one down, pass it around, no more bottles of beer on the wall.\n")
	else:
		print("No more bottles of beer on the wall, no more bottles of beer.")
		print("Go to the store and buy some more, 100 bottles of beer on the wall.")

# Main program
def main():
	try:
		bottles = int(input("Enter number of bottles: "))
		if bottles < 0:
			print("Please enter a positive number of bottles.")
		else:
			countdown(bottles)
	except ValueError:
		print("Invalid input. Please enter a number.")
	print("Remember to buy more beer!")

if __name__ == "__main__":
	main()
