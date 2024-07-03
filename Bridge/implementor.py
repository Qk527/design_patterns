from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render_shape(self, shape):
        pass

class VectorRenderer(Renderer):
    def render_shape(self, shape):
        return f"Drawing {shape.name} as lines"

class RasterRenderer(Renderer):
    def render_shape(self, shape):
        return f"Drawing {shape.name} as pixels"
