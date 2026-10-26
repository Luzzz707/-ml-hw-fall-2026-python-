count = int(input("Enter a positive integer N: "))

numbers = []
for i in range(count):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

x = int(input("Enter an integer X: "))

result = -1
for i, number in enumerate(numbers, start=1):
    if number == x:
        result = i
        break

print(result)
