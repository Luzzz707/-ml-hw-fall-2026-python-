"""Read numbers, then report the 1-based position of a requested value."""


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


def main():
    count = int(input("Enter a positive integer N: "))
    values = NumberList()

    for position in range(1, count + 1):
        values.add(int(input(f"Enter number {position}: ")))

    target = int(input("Enter integer X: "))
    print(values.find_index(target))


if __name__ == "__main__":
    main()
