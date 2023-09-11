def main():
    print(hello())
    name = input("What is your name? ").strip().title()
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"


main()
