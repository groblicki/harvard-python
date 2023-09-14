import csv


def main():
    while True:
        operation = input("[r] Read, [w] Write, [e] Exit\n")
        match operation:
            case "r":
                read()
            case "w":
                write()
            case "e":
                break
            case _:
                pass


def read():
    students = []

    with open("names.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['house']}, lives in {student['home']}")


def write():
    name = input("name: ")
    house = input("house: ")
    home = input("home: ")
    with open("names.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "house", "home"])
        writer.writerow({"name": name, "house": house, "home": home})


if __name__ == "__main__":
    main()

# name = input("name: ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#     for line in file:
#         print(f"hello, {line.rstrip()}")

# with open("names.txt", "r") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"hello, {name}")

# with open("names.csv", "r") as file:
#     for line in file:
#         name, house, home = line.rstrip().split(",")
#         student = {"name": name, "house": house, "home": home}
#         students.append(student)

# with open("names.csv", "r") as file:
#     reader = csv.reader(file)
#     for name, house, home in reader:
#         students.append({"name": name, "house": house, "home": home})
