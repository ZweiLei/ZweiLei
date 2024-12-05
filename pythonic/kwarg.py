def full_name(**kwarg):
    print(kwarg)
    for key, value in kwarg.items():
        print(f"{key} = {value}")

first = input("enter 1st name: ")
sencond = input("enter 2nd name: ")

full_name(first = first, sencond = sencond)
