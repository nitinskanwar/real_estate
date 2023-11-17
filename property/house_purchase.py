"""Combines a house which will be a purchase property
"""
import sys

sys.path.append("real_estate")
from property.house import House
from finances.purchase import Purchase


class HousePurchase(Purchase, House):
    """Combines a house which will be a Purchase property"""

    @staticmethod
    def prompt_init():
        """Prompt the user for inputs and return the inputs as a dictionary.
        this is a class/module level method so it doesn't need a self parameter. it is a static method.
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
