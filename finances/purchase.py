"""This module will be used to create a Purchase class
"""
import sys

sys.path.append("real_estate")


class Purchase:
    """This class will be used to create a Purchase class"""

    def __init__(self, price="", taxes="", **kwargs):
        """Create a purchase instance

        Parameters
        ----------
        price : str, optional
            Describes the price of the property, by default ""
        taxes : str, optional
            Describes the taxes that have to be paid on a property purchase, by default ""
        """
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """Displays the purchase information"""
        # super().display()
        print("Purchase details are as under : ")
        print(f"selling price : {self.price}")
        print(f"estimated taxes : {self.taxes}")

    @staticmethod
    def prompt_init():
        """Gets user input

        Returns
        -------
        dict
            Dictionary containing the user input
        """
        return dict(
            price=input("What is the selling price?"),
            taxes=input("What are the estimated taxes?"),
        )
