#!/usr/bin/python3
"""
Class MyList
"""
class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """


    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        Args:
            None

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)
