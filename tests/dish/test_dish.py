from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish = Dish("Prato-gostoso", 10.0)

    assert dish.name == "Prato-gostoso"
    assert dish.price == 10.0
    assert dish.recipe == dict()

    assert dish == Dish("Prato-gostoso", 10.0)
    assert dish != Dish("Prato-ruim", 20.0)

    assert hash(dish) == hash(Dish("Prato-gostoso", 10.0))
    assert hash(dish) != hash(Dish("Prato-ruim", 20.0))

    assert repr(dish) == "Dish('Prato-gostoso', R$10.00)"

    with pytest.raises(TypeError):
        Dish("Prato-gostoso", "10.0")

    with pytest.raises(ValueError):
        Dish("Prato-gostoso", -10.0)

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Prato-gostoso", 0.0)

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Prato-gostoso", "10.0")

    bacon = Ingredient("bacon")
    frango = Ingredient("frango")

    dish.add_ingredient_dependency(bacon, 100)
    dish.add_ingredient_dependency(frango, 100)

    assert dish.recipe == {bacon: 100, frango: 100}

    assert dish.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }
    assert dish.get_ingredients() == {bacon, frango}
