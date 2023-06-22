import os
import csv

from models.dish import Dish
from models.ingredient import Ingredient

pwd = os.getcwd()
source_path = os.path.join(pwd, "data", "menu_base_data.csv")
print("Sou o source_path", source_path)


def check_file_exists(source_path: str) -> None:
    if not os.path.exists(source_path):
        raise FileNotFoundError("Arquivo não encontrado")


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        check_file_exists(source_path)

        self.source_path = source_path
        self.dishes = self.menu_data()

    def menu_data(self) -> set:
        dishes = dict()

        with open(self.source_path, mode="r", encoding="utf-8") as f:
            r = csv.reader(f)
            next(r)

            for i in r:
                dish_name = i[0]
                price = float(i[1])
                ingredient = i[2]
                amount = int(i[3])

                if dish_name not in dishes:
                    dishes[dish_name] = Dish(dish_name, price)
                dishes[dish_name].add_ingredient_dependency(
                    Ingredient(ingredient), amount
                )

        return set(dishes.values())


if __name__ == "__main__":
    menu_data = MenuData(source_path)

    print(menu_data.dishes)
