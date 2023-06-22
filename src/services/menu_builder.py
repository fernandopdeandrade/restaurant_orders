from typing import Dict, List
from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

# from models.ingredient import Restriction

# import os

# pwd = os.getcwd()
# DATA_PATH = os.path.join(pwd, "data", "menu_base_data.csv")
# INVENTORY_PATH = os.path.join(pwd, "data", "inventory_base_data.csv")

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        menu_list = list()

        dishes = self.menu_data.dishes

        for i in dishes:
            menu_dict = {
                "dish_name": i.name,
                "price": i.price,
                "ingredients": i.get_ingredients(),
                "restrictions": i.get_restrictions(),
            }

            availability = self.inventory.check_recipe_availability(i.recipe)

            if restriction not in menu_dict["restrictions"] and availability:
                menu_list.append(menu_dict)

        return menu_list
