def intersection(a, b):
    return [ item for item in a if item in b ]


if __name__ == "__main__":

    a = [1, 2, 3, 4, 5]
    b = [0, 1, 3, 7]

    intersection = intersection(a, b)
    print(intersection)