from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Set up the Google Sheets API
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('calorietracker')
WORKSHEET = SHEET.worksheet("Entries")
GOALS_WORKSHEET = SHEET.worksheet("Goal")  # Reference to the "Goal" worksheet


@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int

    @classmethod
    def add_food(cls, name, calories, protein, fat, carbs):
        """Create a new food item instance and add it to the list."""
        food = cls(name, calories, protein, fat, carbs)
        today.append(food)
        food.add_to_google_sheets()
        print("Successfully added!")
        return food

    def add_to_google_sheets(self):
        """Append the food entry to the Google Sheets document."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [timestamp, self.name, self.calories, self.protein, self.fat, self.carbs]
        WORKSHEET.append_row(row)
        print("Entry added to Google Sheets successfully.")

    @staticmethod
    def display_daily_analysis():
        """Display the daily analysis as a percentage of the daily goals."""
        if today:
            protein_sum = sum(food.protein for food in today)
            fats_sum = sum(food.fat for food in today)
            carbs_sum = sum(food.carbs for food in today)
            calories_sum = sum(food.calories for food in today)

            protein_percentage = (protein_sum / PROTEIN_GOAL) * 100
            fat_percentage = (fats_sum / FAT_GOAL) * 100
            carbs_percentage = (carbs_sum / CARBS_GOAL) * 100
            calories_percentage = (calories_sum / CALORIE_GOAL) * 100

            print("\nDaily Nutritional Analysis:")
            print(f"Protein: {protein_sum}g ({protein_percentage:.2f}% of goal)")
            print(f"Fats: {fats_sum}g ({fat_percentage:.2f}% of goal)")
            print(f"Carbs: {carbs_sum}g ({carbs_percentage:.2f}% of goal)")
            print(f"Calories: {calories_sum}kcal ({calories_percentage:.2f}% of goal)")

            Food.update_goals_sheet(protein_sum, fats_sum, carbs_sum, calories_sum)
        else:
            print("No foods added yet for today's analysis.")

    @staticmethod
    def update_goals_sheet(protein_sum, fats_sum, carbs_sum, calories_sum):
        """Update the goals worksheet with consumed and goal data."""
        timestamp = datetime.now().strftime("%Y-%m-%d")
        row = [
            timestamp, protein_sum, fats_sum, carbs_sum, calories_sum,
            PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL, CALORIE_GOAL
        ]
        GOALS_WORKSHEET.append_row(row)
        print("Daily consumed data and goals added to the goals worksheet successfully.")

    @staticmethod
    def record_new_goals():
        """Prompt the user to enter new goal values, update them, and display the updated analysis."""
        global PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL, CALORIE_GOAL

        try:
            protein_goal = int(input("Enter your new protein goal: "))
            fat_goal = int(input("Enter your new fat goal: "))
            carbs_goal = int(input("Enter your new carb goal: "))
            calorie_goal = int(input("Enter your new calorie goal: "))

            # Update local goals
            PROTEIN_GOAL = protein_goal
            FAT_GOAL = fat_goal
            CARBS_GOAL = carbs_goal
            CALORIE_GOAL = calorie_goal
            print("New goals set successfully.\n")

            # Display updated daily analysis with new goals
            Food.display_daily_analysis()

        except ValueError:
            print("Please enter valid numbers for each goal.")


# Main Program
today = []  # List to store daily food entries
done = False

while not done:
    print("""
    (1) Add your dinner
    (2) Display your nutritional analysis
    (3) Record new daily goals
    (q) Quit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Name: ")

        try:
            calories = int(input("Calories: "))
            protein = int(input("Protein: "))
            fat = int(input("Fats: "))
            carbs = int(input("Carbs: "))

            # Add food instance and save it
            Food.add_food(name, calories, protein, fat, carbs)

        except ValueError:
            print("Please enter numeric values for calories, protein, fats, and carbs.")

    elif choice == "2":
        Food.display_daily_analysis()

    elif choice == "3":
        Food.record_new_goals()

    elif choice.lower() == 'q':
        done = True
        print("Great job! You've successfully logged all your calories for the day!")

    else:
        print("Invalid choice, please try again.")
