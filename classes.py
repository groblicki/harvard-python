import random


class Hat:
    _houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls):
        return random.choice(cls._houses)


class Wizard:
    def __init__(self, name, patronus):
        self.name = name
        self.patronus = patronus

    def __add__(self, other):
        return f"{self.name} knows {other.name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def patronus(self):
        return self._patronus

    @patronus.setter
    def patronus(self, patronus):
        self._patronus = patronus

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐕"
            case _:
                return "🪄"


class Professor(Wizard):
    def __init__(self, name, patronus, subject):
        super().__init__(name, patronus)
        self.subject = subject

    def __str__(self):
        return f"{self.name} teaches {self.subject}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        patronus = input("Patronus: ")
        subject = input("Subject: ")
        return cls(name, patronus, subject)

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        self._subject = subject


class Student(Wizard):
    def __init__(self, name, patronus, house):
        super().__init__(name, patronus)
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        patronus = input("Patronus: ")
        house = Hat.sort()
        return cls(name, patronus, house)

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = Student.get()
    print(student)
    print("Expecto Patronum!")
    print(student.charm())
    professor = Professor.get()
    print(professor)
    print("Expecto Patronum!")
    print(professor.charm())
    print(student + professor)


if __name__ == "__main__":
    main()
