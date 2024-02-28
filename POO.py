class Pessoa:
    def __init__(self, name, ender):
        self.set_name(name)
        self.set_ender(ender)

    def set_name(self, name):
        self.name = name

    def set_ender(self, ender):
        self.ender = ender

    def get_name(self):
        return self.name

    def get_ender(self):
        return self.ender


Pessoa1 = Pessoa("maria", "rua professorwaldey de almeida")
print(f'Name: {Pessoa1.get_name()}, Endereço: {Pessoa1.get_ender()}')