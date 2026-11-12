def draw_pattern(n):
    """
    Recursively prints an inverted triangle of asterisks.

    Parameters:
    n (int): The starting number of asterisks in the top row.
    """
    if n <= 0:
        return
    print("*" * n)
    draw_pattern(n - 1)
    if n > 1:
        print("*" * n)


if __name__ == "__main__":
    draw_pattern(3)