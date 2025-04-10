class Retangulo:
  def __init__(self, largura1, largura2, comprimento1, comprimento2):
    self.largura1 = largura1
    self.largura2 = largura2
    self.comprimento1 = comprimento1
    self.comprimento2 = comprimento2

  def analisar(self):
    if (self.largura1 == self.largura2) and (self.comprimento1 == self.comprimento2):
      return "Sim, é um retangulo"
    else:
      return "Não, não é um retangulo"

retangulo01 = Retangulo(1, 1, 2, 2)
print(retangulo01.analisar())

retangulo02 = Retangulo(1, 2, 3, 4)
print(retangulo02.analisar())