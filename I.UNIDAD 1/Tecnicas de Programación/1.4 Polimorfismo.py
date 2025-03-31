class Instrumento:
    def tocar(self):
        pass

class Guitarra(Instrumento):
    def tocar(self):
        return "Tocando la guitarra"

class Piano(Instrumento):
    def tocar(self):
        return "Tocando el piano"

class Bateria(Instrumento):
    def tocar(self):
        return "Tocando la batería"

def tocar_instrumento(instrumento):
    return instrumento.tocar()

# Uso
guitarra = Guitarra()
piano = Piano()
bateria = Bateria()

instrumentos = [guitarra, piano, bateria]

for instrumento in instrumentos:
    print(tocar_instrumento(instrumento))