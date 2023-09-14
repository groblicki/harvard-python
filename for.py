def main():
    meow(get_number())

    # print("meow\n" * 3, end="")


def get_number():
    while True:
        i = int(input("i: "))
        if i >= 0:
            return i


def meow(n):
    for _ in range(n):
        print("meow")


main()
