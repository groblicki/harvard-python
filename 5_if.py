def main():
    x = int(input("x: "))
    y = int(input("y: "))
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")

    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

    score = int(input("Score: "))
    if 90 >= score <= 100:
        print("Grade: A")
    elif 80 <= score < 90:
        print("Grade: B")
    elif 70 <= score < 80:
        print("Grade: C")
    elif 60 <= score < 70:
        print("Grade: D")
    elif 0 <= score < 60:
        print("Grade: F")
    else:
        print("Enter the correct score [0-100]")


def is_even(n):
    return n % 2 == 0  # bool


main()
