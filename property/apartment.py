"""
This class will be used to create an apartment object. It will inherit from the Property class.
"""
import sys

sys.path.append("real_estate")
from property.property import Property


class Apartment(Property):
    """
    This class will be used to create an apartment object. It will inherit from the Property class.
    """

    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony="", laundry="", **kwargs):
        """Initialize the Apartment object. The kwargs will be used to initialize the superclass.
        We are doing this so that we can inherit from this class downstream in case of multiple inheritance.

        Parameters
        ----------
        balcony : str, optional
            Describes if the apartment has a balcony or not, by default ""
        laundry : str, optional
            Describes if the apartment has a laundry or not, by default ""
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """Display the apartment information."""
        super().display()
        print("Apartment Details are as under : ")
        print(f"laundry : {self.laundry}")
        print(f"has balcony : {self.balcony}")

    @staticmethod
    def prompt_init():
        """Prompt the user for inputs and return the inputs as a dictionary.
        This is a class/module level method so it doesn't need a self parameter. It is a static method.
        """

        parent_init = Property.prompt_init()
        laundry = ""
        balcony = ""
        laundry = Apartment.get_valid_input(
            "What kind of laundry facilities does the property have?",
            Apartment.valid_laundries,
        )
        balcony = Apartment.get_valid_input(
            "What kind of balconies does the property have?",
            Apartment.valid_balconies,
        )
        parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init

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
