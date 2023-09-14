def main():
    snakes = {"Ebony": "ssss", "Fluffy": "ss", "Jafaar": None, "Medusa": "sss"}

    for snake in snakes:
        if snakes[snake]:
            print(f"{snake} says {snakes[snake]}")
        else:
            print(f"{snake} says nothing")

    # for i in range(len(cats)):
    #     print(f"{cats[i]} says meow")

    animals = [
        {"name": "Poppy", "sound": "meow", "color": "gray"},
        {"name": "Bella", "sound": "meow", "color": "black"},
        {"name": "Misty", "sound": "woof", "color": "brown"},
        {"name": "Molly", "sound": "meow", "color": "white"},
    ]

    for animal in animals:
        print(
            f"{animal['color'].capitalize()} {animal['name']} says {animal['sound']}."
        )


main()
