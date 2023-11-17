"""This module creates agents which will buy, rent and sell properties.
"""

import sys

sys.path.append("real_estate")

from property.apartment_purchase import ApartmentPurchase
from property.apartment_rental import ApartmentRental
from property.house_purchase import HousePurchase
from property.house_rental import HouseRental


class Agent:
    """Agent class which will buy, sell and rent properties."""

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase,
    }

    def __init__(self):
        self.list_of_properties = []

    def display_properties(self):
        """Displays the list of properties"""
        for propert in self.list_of_properties:
            propert.display()

    def add_property(self):
        """Adds a property to the list of properties"""
        property_type = Agent.get_valid_input(
            "What type of property? ", ("house", "apartment")
        ).lower()
        payment_type = Agent.get_valid_input(
            "What payment type? ", ("purchase", "rental")
        ).lower()
        property_class = self.type_map[(property_type, payment_type)]
        init_args = property_class.prompt_init()
        self.list_of_properties.append(property_class(**init_args))

    @staticmethod
    def get_valid_input(input_string, input_values):
        """Returns the correct input from the user after comparing with the predefined values.

        Parameters
        ----------
        input_string : string
            Input prompt for the user
        input_values : tuple
            Predefined values defined as class variables. The user input will be compared with these values.

        Returns
        -------
        string
            The user input after comparing with the predefined values.
        """
        input_string += f" ({', '.join(input_values)}) : "
        response = ""
        while response.lower() not in input_values:
            response = input(input_string)
        return response
