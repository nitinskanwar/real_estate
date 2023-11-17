"""
This class will be used to create a house object. It will inherit from the Property class.
"""
import sys

sys.path.append("real_estate")
from property.property import Property


class House(Property):
    """
    This class will be used to create a house object. It will inherit from the Property class.
    """

    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, garage="", fence="", number_of_stories="", **kwargs):
        """Initialize the House object. The kwargs will be used to initialize the superclass.
        We are doing this so that we can inherit from this class downstream in case of multiple inheritance.

        Parameters
        ----------
        garage : str, optional
            Describes if the house has a garage or not, by default ""
        fence : str, optional
            Describes if the house has a fence or not, by default ""
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fence = fence
        self.number_of_stories = number_of_stories

    def display(self):
        """Display the house information."""
        super().display()
        print("House details are as under : ")
        print(f"garage : {self.garage}")
        print(f"has fence : {self.fence}")
        print(f" and has number of stories : {self.number_of_stories}")

    @staticmethod
    def prompt_init():
        """Prompt the user for inputs and return the inputs as a dictionary.
        this is a class/module level method so it doesn't need a self parameter. it is a static method.
        """

        parent_init = (
            Property.prompt_init()
        )  # Super will not work here since the method is a static method
        garage = ""
        fence = ""
        number_of_stories = ""
        garage = House.get_valid_input(
            "What kind of garage does the property have?",
            House.valid_garage,
        )
        fence = House.get_valid_input(
            "Is the property fenced?",
            House.valid_fenced,
        )
        number_of_stories = input("How many stories? ")
        parent_init.update(
            {"garage": garage, "fence": fence, "number_of_stories": number_of_stories}
        )
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
