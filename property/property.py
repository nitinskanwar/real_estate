"""
This class will be used to create a property object.
"""
import sys

sys.path.append("real_estate")


class Property:
    """This class will be used to create a property object. It will be inherited downstream so we need to add kwwargs to the init method.

    Parameters
    ----------
    object : Object Superclass
        This is the built in Object superclass in Python. It is the superclass of all other classes. It is used to create a new class that does not inherit from any other class. It is the most base type.
    """

    def __init__(self, square_feet="", beds="", baths="", **kwargs):
        """Initialize the Property object. The kwargs will be used to initialize the superclass.
        We are doing this so that we can inherit from this class downstream in case of multiple inheritance.

        Parameters
        ----------
        square_feet : str, optional
            Provides the square footage of the property, by default ""
        beds : str, optional
            Describes the number of bedrooms in the property, by default ""
        baths : str, optional
            Describes the number of bathrooms in the property, by default ""
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_bathrooms = baths

    def display(self):
        """Display the property information."""
        print("Property Details are as under : ")
        print(f"Square Footage is {self.square_feet}")
        print(f"Number of Bedrooms are {self.num_bedrooms}")
        print(f"Number of Bathrooms are {self.num_bathrooms}")
        print()

    @staticmethod
    def prompt_init():
        """Prompt the user for inputs and return the inputs as a dictionary."""
        return dict(
            square_feet=input("Enter the square feet : "),
            beds=input("Enter the number of bedroooms : "),
            baths=input("Enter the number of bathrooms : "),
        )

    # This is another way to declare a static method. The above method of
    # using a decorator is more common.
    prompt_init = staticmethod(prompt_init)
