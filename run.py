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

    def add_to_google_sheets(self, food: Food):
        """Appends a food entry to Google Sheets."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [timestamp, food.name, food.calories, food.protein, food.fat, food.carbs]
        WORKSHEET.append_row(row)
        print("Entry added to Google Sheets successfully.")

    def update_goals_sheet(self):
        """Updates Google Sheets with consumed and goal data for the day."""
        protein_sum = sum(food.protein for food in self.today)
        fats_sum = sum(food.fat for food in self.today)
        carbs_sum = sum(food.carbs for food in self.today)
        
        timestamp = datetime.now().strftime("%Y-%m-%d")
        row = [timestamp, protein_sum, fats_sum, carbs_sum, self.protein_goal, self.fat_goal, self.carbs_goal]
        GOALS_WORKSHEET.append_row(row)
        print("Daily consumed data and goals added to the goals worksheet successfully.")

    def record_new_goals(self):
        """Prompts the user for new goals and updates the goals worksheet."""
        try:
            self.protein_goal = int(input("Enter your new protein goal: "))
            self.fat_goal = int(input("Enter your new fat goal: "))
            self.carbs_goal = int(input("Enter your new carb goal: "))

            self.update_goals_sheet()
            print("New goals set and logged successfully.")
            
        except ValueError:
            print("Please enter valid numbers for each goal.")

    def main_menu(self):
        """Displays the main menu and processes user choices."""
        done = False
        while not done:
            print("""
            (1) Add your dinner
            (2) Record new daily goals
            (q) Quit
            """)
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                name = input("What did you have for dinner? Name: ")
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
                
            elif choice.lower() == 'q':
                done = True
                print("Great job! You've successfully logged all your calories for the day!")
                
            else:
                print("Invalid choice, please try again.")
# Run the application
if __name__ == "__main__":
    tracker = FoodTracker()
    tracker.main_menu()
                
