from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe) -> bool:
        for ingredient in recipe:
            if self.inventory.get(ingredient, 0) < recipe[ingredient]:
                return False

        return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        check = self.check_recipe_availability(recipe)

        if not check:
            raise ValueError("Recipe not available")

        for ingredient in recipe:
            self.inventory[ingredient] -= recipe[ingredient]