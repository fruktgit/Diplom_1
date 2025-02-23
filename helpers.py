from Praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def get_sauces(ingredients):
    """Фильтрует список ингредиентов, оставляя только соусы."""
    return [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]

def get_fillings(ingredients):
    """Фильтрует список ингредиентов, оставляя только начинки."""
    return [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]

def get_ingredient_prices(ingredients):
    """Создает словарь с ценами ингредиентов."""
    return {i.get_name(): i.get_price() for i in ingredients}