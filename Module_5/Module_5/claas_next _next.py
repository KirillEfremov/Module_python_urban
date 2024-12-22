class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to (self, new_floor):
        for i in range(1, new_floor + 1):
            if i >= 1:
                print(i)
            if i >= self.number_of_floors:
                print('Такого этажа не существует')
                break
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def  __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def __radd__(self, value):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def __iadd__(self, value):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

# __eq__
print(h1==h2)

# __lt__
print(h1 < h2)
# __le__
print(h1 <= h2)
# __gt__
print(h1 > h2)
# __ge__
print(h1 >= h2)
# __ne__
print(h1 != h2)

# __add__
h1.number_of_floors = h1.number_of_floors + 10
print(h1)
# __radd__
h2.number_of_floors = 10 + h2.number_of_floors
print(h2)
# __iadd__
h1.number_of_floors += 10
print(h1)

