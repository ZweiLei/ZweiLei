def binary_dec(binary_list):
     string = "".join(map(str, binary_list))
     dec = int(string, 2)
     return dec

if __name__ == "__main__":
     binary_list = list(map(int, input().split()))
     print(binary_dec(binary_list))