from abstraction import Circle
from implementor import VectorRenderer, RasterRenderer

if __name__ == "__main__":
  vector_circle = Circle(VectorRenderer(), radius: 5)
  raster_circle = Circle(RasterRenderer(), radius: 5)

  print(vector_circle.draw())
  print(raster_circle.draw())
