class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

p2 = Person("Chuck", 21)

print(p2.name)
print(p2.age)
