"""This module will be used to create a Rental class
"""
import sys

sys.path.append("real_estate")


class Rental:
    """This class will be used to create a Rental class"""

    def __init__(self, furnished="", utilities="", rent="", **kwargs):
        """Initialize a Rental class

        Parameters
        ----------
        furnished : str, optional
            Is the house furnished, by default ""
        utilities : str, optional
            What are the utilities, by default ""
        rent : str, optional
            What is the rent, by default ""
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        """Displays the Rental information"""
        super().display()
        print("Rental details are as under : ")
        print(f"rent : {self.rent}")
        print(f"estimated utilities : {self.utilities}")
        print(f"furnished : {self.furnished}")

    @staticmethod
    def prompt_init():
        """Gets user input

        Returns
        -------
        dict
            Dictionary containing the user input
        """
        return dict(
            furnished=input("Is the house furnished?"),
            utilities=input("What are the estimated utilities?"),
            rent=input("What are the estimated rent?"),
        )
