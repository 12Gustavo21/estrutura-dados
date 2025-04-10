class Ponto:
  def __init__(self, x, y):
    self.x=x
    self.y=y
  
  def quadrante(self):
    if self.x > 0 and self.y > 0:
      return "Q1"
    elif self.x < 0 and self.y > 0:
      return "Q2"
    elif self.x < 0 and self.y < 0:
      return "Q3"
    elif self.x > 0 and self.y < 0:
      return "Q4"
    else:
      return "Nenhum dos quadrantes"

while True:

  x, y = int(input("x = ")), int(input("y = "))
  
  if x == 0 and y == 0:
    break
  
  p = Ponto(x,y)
  print(f"Coordenadas do ponto 1: {p.x}, {p.y}")
  print(f"O ponto 1 pertence ao quadrante: {p.quadrante()}\n")