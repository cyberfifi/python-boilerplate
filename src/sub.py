import pandas as pd


def run():
    data = pd.read_csv("./resources/nyc-rolling-sales.csv")
    print(data)


def add(x, y):

    """Add two numbers.
    :params x: int, first number to add
    :params y: int, second number to add
    :returns: int, the sum of the two numbers
    """
    return x + y
