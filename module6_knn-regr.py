"""Interactive k-NN regression using NumPy."""

import numpy as np


def read_positive_integer(prompt: str) -> int:
    """Read an integer greater than zero, retrying until the input is valid."""
    while True:
        raw_value = input(prompt)
        try:
            value = int(raw_value)
        except ValueError:
            print("Please enter a positive integer.")
            continue

        if value <= 0:
            print("Please enter a positive integer.")
            continue

        return value


def read_real_number(prompt: str) -> float:
    """Read a real number, retrying until the input is valid."""
    while True:
        raw_value = input(prompt)
        try:
            return float(raw_value)
        except ValueError:
            print("Please enter a real number.")


def knn_regression(points: np.ndarray, query_x: float, k: int) -> float:
    """Return the mean y-value of the k points nearest to query_x."""
    # Only x is an input feature, so the distance is |query_x - point_x|.
    distances = np.abs(points[:, 0] - query_x)
    nearest_indices = np.argsort(distances, kind="stable")[:k]
    return float(np.mean(points[nearest_indices, 1]))


def main() -> None:
    n = read_positive_integer("Enter N (number of points, a positive integer): ")
    k = read_positive_integer("Enter k (number of neighbors, a positive integer): ")

    # Each row stores one point as [x, y]. NumPy holds and processes the data.
    points = np.empty((n, 2), dtype=float)
    for index in range(n):
        print(f"Enter point {index + 1}:")
        points[index, 0] = read_real_number("  x = ")
        points[index, 1] = read_real_number("  y = ")

    query_x = read_real_number("Enter the input X: ")

    if k > n:
        print(f"Error: k ({k}) cannot be greater than N ({n}).")
        return

    predicted_y = knn_regression(points, query_x, k)
    print(f"Predicted Y: {predicted_y}")


if __name__ == "__main__":
    main()
