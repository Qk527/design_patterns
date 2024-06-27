from factory import ChessPieceFactory

def main():
  piece1 = ChessPieceFactory.get_flyweight(name:'Rook', color:'Black')
  piece2 = ChessPieceFactory.get_flyweight(name:'Rook', color:'Black')

  print(piece1 is piece2)
  
  piece1.display("A8")
  piece2.display("H8")

if __name__ == "__main__":
  main()
