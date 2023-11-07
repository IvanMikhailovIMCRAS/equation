def eq(a: float, b: float) -> float:
    if a == 0:
        raise ValueError("a must not be equal 0")
    if b == 0:
        raise ValueError("a lot of solutions")
    return -b / a


if __name__ == "__main__":
    print(eq(1, 0))
