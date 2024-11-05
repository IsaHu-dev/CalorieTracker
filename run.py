from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('CalorieTracker')


today = []  # List to store daily food entries


# Define a data class to represent a food item with its nutritional values
@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int

PROTEIN_GOAL = 100
FAT_GOAL = 70
CARBS_GOAL = 300

done = False  # Control variable to exit the main loop

# Main program loop
while not done:
    # Display menu options
    print("""
    (1) Add your dinner
    (2) View the visualisation graph
    (q) Quit
    """)

    choice = input("Enter your choice:")  # Get user input for choice

    if choice == "1":
        # Adding a food item
        print("What did you have for dinner?")
        name = input("Name: ")

        try:
            # Input for nutritional values
            calories = int(input("Calories: "))
            protein = int(input("Protein: "))
            fats = int(input("Fats: "))
            carbs = int(input("Carbs: "))

            # Create a Food instance and add it to the list
            food = Food(name, calories, protein, fats, carbs)
            today.append(food)
            print("Successfully added!")
        except ValueError:
            # Handle non-numeric inputs
            print("Please enter numeric values for calories, protein, fats, and carbs.")
    elif choice == "2":
        # Visualize nutritional progress
        if today:
            # Summing up the nutrients from the foods added today
            calorie_sum = sum(food.calories for food in today)
            protein_sum = sum(food.protein for food in today)
            fats_sum = sum(food.fat for food in today)
            carbs_sum = sum(food.carbs for food in today)

            # Create a pie chart for macronutrient distribution
            fig, axs = plt.subplots(2, 2)
            axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=['Protein', 'Fats', 'Carbs'], autopct="%1.1f%%")
            axs[0, 0].set_title("Macronutrient Forecast")
            axs[0, 1].bar([0.5,1.5,2.5], [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width=0.4)
            axs[0, 1].set_title("Macronutrients Progress")


            fig.tight_layout()  # Adjust layout to prevent overlap
            plt.show()  # Display the plot
        else:
            # If no foods have been added yet
            print("No foods added yet to visualize progress.")
    elif choice.lower() == 'q':
        # Exit the program
        done = True
        print("You're all set, all calories logged for the day.")
    else:
        # Handle invalid input
        print("Invalid choice, please try again.")
