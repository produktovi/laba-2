class cifra:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        if isinstance(other, cifra):
            return cifra(self.value + other.value)
        else:
            return cifra(self.value + other)
    def __radd__(self, other):
        return self.__add__(other)
a = cifra(5)
b = cifra(10)
print((a + b).value) #Вывод 15
print((a + 2).value) #Вывод 7
print((3 + a).value) #Вывод 8