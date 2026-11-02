"""Interactive program using the NumberList class from module5_mod."""

from module5_mod import NumberList


def main():
    count = int(input("Enter a positive integer N: "))
    values = NumberList()

    for position in range(1, count + 1):
        values.add(int(input(f"Enter number {position}: ")))

    target = int(input("Enter integer X: "))
    print(values.find_index(target))


if __name__ == "__main__":
    main()
