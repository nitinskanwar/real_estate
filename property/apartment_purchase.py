"""Combines an apartment which will be a purchase property
"""
import sys
from property.apartment import Apartment

sys.path.append("real_estate")

from finances.purchase import Purchase


class ApartmentPurchase(Purchase, Apartment):
    """Combines a Apartment which will be a Purchase property"""

    @staticmethod
    def prompt_init():
        """Prompt the user for inputs and return the inputs as a dictionary.
        this is a class/module level method so it doesn't need a self parameter. it is a static method.
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
