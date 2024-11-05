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
