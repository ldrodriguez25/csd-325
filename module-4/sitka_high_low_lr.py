# Luis Rodriguez
# June 25 2026
# CSD-325 Module 4.2 Assignment
#
# Purpose: Display Sitka weather high or low temperatures based on
# user selection and continue running until the user chooses to exit.

import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys

# CSV file containing Sitka weather data
filename = 'sitka_weather_2018_simple.csv'

# Continue displaying the menu until the user exits
while True:

    # Display the program menu
    print("\n===== Sitka Weather Menu =====")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")

    user_choice = input("Enter your choice (1-3): ")

    # Exit the program
    if user_choice == '3':
        print("\nThank you for using the Sitka Weather program. Goodbye!")
        sys.exit()

    # Display high temperatures
    elif user_choice == '1':

        # Open the CSV file and read the data
        with open(filename) as weather_file:
            reader = csv.reader(weather_file)
            header_row = next(reader)

            dates = []
            temperatures = []

            # Read each row from the CSV file
            for row in reader:
                current_date = datetime.strptime(
                    row[2], '%Y-%m-%d'
                )
                high_temperature = int(row[5])

                dates.append(current_date)
                temperatures.append(high_temperature)

        # Create the high temperature graph
        fig, ax = plt.subplots()
        ax.plot(dates, temperatures, c='red')

        plt.title(
            'Daily High Temperatures - Sitka, 2018',
            fontsize=20
        )
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel('Temperature (F)', fontsize=16)
        plt.tick_params(axis='both',
                        which='major',
                        labelsize=12)

        plt.show()

    # Display low temperatures
    elif user_choice == '2':

        # Open the CSV file and read the data
        with open(filename) as weather_file:
            reader = csv.reader(weather_file)
            header_row = next(reader)

            dates = []
            temperatures = []

            # Read each row from the CSV file
            for row in reader:
                current_date = datetime.strptime(
                    row[2], '%Y-%m-%d'
                )
                low_temperature = int(row[6])

                dates.append(current_date)
                temperatures.append(low_temperature)

        # Create the low temperature graph
        fig, ax = plt.subplots()
        ax.plot(dates, temperatures, c='blue')

        plt.title(
            'Daily Low Temperatures - Sitka, 2018',
            fontsize=20
        )
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel('Temperature (F)', fontsize=16)
        plt.tick_params(axis='both',
                        which='major',
                        labelsize=12)

        plt.show()

    # Handle invalid menu choices
    else:
        print("\nInvalid selection. Please enter 1, 2, or 3.")