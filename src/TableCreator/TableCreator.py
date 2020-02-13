import random
from sys import path

def random_name():
    names = ["John", "Joshua", "Andrew", "Sergei", "Alina", "Stas", "Lera",  "Iana", "Kostya", "Evghen", "Dima",
             "Maria", "Anna", "Vasea", "Ulian", "Olga", "Liza", "Mihail", "Valera", "Kristi", "Amily", "Rory",
             "William", "Alex"]
    return random.choice(names)


def random_salary():
    return str(random.randrange(3000, 10000))


def random_position():
    position = ["Clerk", "Director", "Receptionist", "Secretary", "Lawyer", "Accountant", "Cashier"]
    return random.choice(position)


def random_work():
    return str(random.randrange(1, 7))


def random_child():
    return str(random.randint(0, 3))


if __name__ == "__main__":
    file = open("Result", "w+")

    # file.writelines("№\t\t" + "Name\t\t" + "Salary\t\t" + "Position\t\t" + "Years\t\t" + "Child\n")
    for number in range(1, 51):
        
        file.writelines(random_name() + "\t\t" + random_salary() + "\t\t"
                        + random_position() + "\t\t" + random_work() + "\t\t\t" + random_child() + "\n")

    file.close()
