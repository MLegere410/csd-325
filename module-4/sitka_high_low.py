# Madison Legere, 11/10/2024, Module 4.2

import matplotlib.pyplot as plt
import sys

# Sample data
dates = ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04']
highs = [45, 47, 50, 46]
lows = [30, 28, 32, 31]

def plot_temperatures(option):
    if option == 'highs':
        plt.plot(dates, highs, color='red')
        plt.title('High Temperatures')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°F)')
    elif option == 'lows':
        plt.plot(dates, lows, color='blue')
        plt.title('Low Temperatures')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°F)')
    plt.show()

def main():
    while True:
        print("\nSelect an option:")
        print("1. Highs")
        print("2. Lows")
        print("3. Exit")

        choice = input("Enter your choice: ").lower()

        if choice == '1' or choice == 'highs':
            plot_temperatures('highs')
        elif choice == '2' or choice == 'lows':
            plot_temperatures('lows')
        elif choice == '3' or choice == 'exit':
            print("Thank you for using the weather program. Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please choose again.")

if __name__ == "__main__":
    main()
