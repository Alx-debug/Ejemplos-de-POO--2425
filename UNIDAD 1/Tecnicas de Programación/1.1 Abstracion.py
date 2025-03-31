from abc import ABC, abstractmethod

class Electrodomestico(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

class Televisor(Electrodomestico):
    def encender(self):
        return "El televisor está encendido"

    def apagar(self):
        return "El televisor está apagado"

class Lavadora(Electrodomestico):
    def encender(self):
        return "La lavadora está en funcionamiento"

    def apagar(self):
        return "La lavadora se ha detenido"

# Uso
tv = Televisor()
lavadora = Lavadora()

print(tv.encender())
print(lavadora.encender())
print(tv.apagar())
print(lavadora.apagar())