"""Combines apartment which will be a rental property
"""
import sys

sys.path.append("real_estate")
from property.apartment import Apartment
from finances.rental import Rental


class ApartmentRental(Rental, Apartment):
    """Combines a house which will be a rental property"""

    @staticmethod
    def prompt_init():
        """Prompt the user for inputs and return the inputs as a dictionary.
        this is a class/module level method so it doesn't need a self parameter. it is a static method.
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
