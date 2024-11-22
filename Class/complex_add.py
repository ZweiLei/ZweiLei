class Complex:
    def __init__(self, real, imag) -> None:
        self.real = real
        self.imag = imag

    def add(self, number):
        re_real = self.real + number.real
        re_imag = self.imag + number.imag
        return Complex(re_real, re_imag)
    
if __name__ == "__main__":
    n1 = Complex(3, 4)
    n2 = Complex(-2, 8)
    n3 = n1.add(n2)
    print(n3.real, n3.imag)
