def count_evens(nums: list) -> int:
    c = 0
    for i in nums:
        if i % 2 == 0:
            c += 1
    return c

if __name__ == "__main__":
    nums = eval(input("Enter a nums list: "))
    print(f"Total number of evens in the list: {count_evens(nums)}")
