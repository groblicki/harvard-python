def main():
    print(f"x is {get_int('x: ')}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
            # print("x is not an integer")
        # else:
        #     return x


main()
