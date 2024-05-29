# Suponemos un objeto de texto al que le vamos a agregar etiquetas HTML

from abc import ABC, abstractmethod

class Text(ABC):
    @abstractmethod
    def render(self):
        pass
