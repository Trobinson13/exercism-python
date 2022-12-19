"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """
    Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake.
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    _bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return _bake_time_remaining
    
def preparation_time_in_minutes(number_of_layers: int) -> int:
    """
    Calculate total amount of time it takes to prepare the recipe.

    :param number_of_layers: int number of layers in the lasagna.
    :return: int total amount of time (in minutes) it will take to prepare the recipe.

    Function that takes the number of layers in a recipe as an argument and returns the total 
        amount of minutes needed to prepare the recipe based on the `PREPARATION_TIME` multiplied by `number_of_layers`.
    """
    
    if number_of_layers >= 1:
        _preparation_time_in_minutes = (number_of_layers * PREPARATION_TIME)
        return _preparation_time_in_minutes
    else:
        raise Exception("Number of layers must be greater than 0")

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """
    Calculate elaplsed time it has taken to make the recipe.

    :param number_of_layers: int number of layers in the lasagna
    :param elapsed_bake_time: int number of minutes that recipe has spent baking thus far.
    :return: int total number of minutes that have been passed in both baking and preperation of recipe.
    
    Funtion that calculates the total preparation in minutes (preparation_time_in_minutes) from total numbers of layers (parsed number_of_layers) and returns _elapsed_time_in_minutes (the total sum of preparation_time_in_minutes + elapsed_bake_time).
    """
    _elapsed_time_in_minutes = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    
    return _elapsed_time_in_minutes