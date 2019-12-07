kind = "blank"

def test_kind():
    print("Test Kind:", kind)

class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name

    def what_kind(self):
        print("Name:", self.name)
        kind = "teste 2"
        print("Geral:", kind)
        print("Self:", self.kind)

# Testes...
d = Dog('Fido')
e = Dog('Buddy')

test_kind()
print('-' * 40)

Dog.kind = "teste 123"
d.what_kind()
print('-' * 40)
e.what_kind()
print('-' * 40)

print("Depois de atribuido:", kind)

print(Dog)
print(Dog.what_kind)
print(e)
print(e.what_kind)