def main():
    x = int(input("x: "))
    print(f"{x} ^ 2 = {square(x)}")
    name = input("name: ")
    print(hello(name))


def square(n):
    return n * n


def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()
