from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

today = []  # List to store daily food entries


# Define a data class to represent a food item with its nutritional values
@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int


done = False  # Control variable to exit the main loop

# Main program loop
while not done:
    # Display menu options
    print("""
    (1) Add your dinner
    (2) Visualize progress
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
            axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=['Protein', 'Fats', 'Carbs'])
            axs[0, 0].set_title("Macronutrient Forecast")

            fig.tight_layout()  # Adjust layout to prevent overlap
            plt.show()  # Display the plot
