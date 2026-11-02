"""Reusable OOP storage and search for integer values."""


class NumberList:
    """Store integers and find the first position of a value."""

    def __init__(self):
        self.numbers = []

    def add(self, number):
        """Add one integer to the list."""
        self.numbers.append(number)

    def find_index(self, value):
        """Return the first 1-based position of value, or -1 if absent."""
        try:
            return self.numbers.index(value) + 1
        except ValueError:
            return -1
