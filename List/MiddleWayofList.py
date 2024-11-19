def middle_way(a: list, b: list) -> list:
    return a[1:-1] + b[1:-1]

if __name__ == "__main__":
    a, b = eval(input("enter two number lists: "))
    print(middle_way(a, b))