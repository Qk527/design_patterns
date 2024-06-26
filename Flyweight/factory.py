class ChessPieceFactory:
  _flyweights = {}

  @classmethod
  def get_flyweight(cls, name,color):
    key = (name, color)
    if not cls._fliyweights.get(key):
      cls._fliyweights[key] = ChessPieceFlyweight(name, color)
    return cls._flyweights[key]
