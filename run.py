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

class FoodTracker:
    def __init__(self):
        self.today = []  # Stores daily food entries
        self.protein_goal = 100
        self.fat_goal = 70
        self.carbs_goal = 300

    def add_food(self, food: Food):
        """Adds a food entry to the list and logs it in Google Sheets."""
        self.today.append(food)
        self.add_to_google_sheets(food)
        print("Successfully added!")

    # Other existing methods go here...

    def calculate_weekly_totals(self):
        """Calculates and displays the weekly total calories and macronutrients."""
        total_calories = sum(food.calories for food in self.today) * 7
        total_protein = sum(food.protein for food in self.today) * 7
        total_fat = sum(food.fat for food in self.today) * 7
        total_carbs = sum(food.carbs for food in self.today) * 7

        print("\nWeekly Totals:")
        print(f"Total Calories: {total_calories}")
        print(f"Total Protein: {total_protein}g")
        print(f"Total Fat: {total_fat}g")
        print(f"Total Carbs: {total_carbs}g\n")

    def main_menu(self):
        """Displays the main menu and processes user choices."""
        done = False
        while not done:
            print("""
            (1) Add your dinner
            (2) Record new daily goals
            (3) Review your daily goal's analysis
            (4) Calculate weekly totals
            (q) Quit
            """)
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                name = input("What did you have for dinner? Food Item: ")
                try:
                    calories = int(input("Calories: "))
                    protein = int(input("Protein: "))
                    fat = int(input("Fats: "))
                    carbs = int(input("Carbs: "))
                    food = Food(name, calories, protein, fat, carbs)
                    self.add_food(food)
                except ValueError:
                    print("Please enter numeric values (round numbers) for calories, protein, fats, and carbs.")
                    
            elif choice == "2":
                self.record_new_goals()
                
            elif choice == "3":
                self.calculate_goal_percentage()

            elif choice == "4":
                self.calculate_weekly_totals()
                
            elif choice.lower() == 'q':
                done = True
                print("Great job! You've successfully logged all your calories for the day!")
                
            else:
                print("Invalid choice, please try again.")

# Run the application
if __name__ == "__main__":
    tracker = FoodTracker()
    tracker.main_menu()
