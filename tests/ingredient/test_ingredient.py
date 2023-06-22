from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("presunto")

    assert ingredient.name == "presunto"
    assert ingredient == Ingredient("presunto")
    assert ingredient != Ingredient("queijo")

    assert repr(ingredient) == "Ingredient('presunto')"
    assert hash(ingredient) == hash("presunto")

    assert ingredient.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
