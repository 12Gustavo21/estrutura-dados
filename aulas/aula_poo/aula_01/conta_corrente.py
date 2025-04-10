class Conta_Corrente:
  def __init__(self, numero, saldo, agencia):
    self.numero = numero
    self.saldo = saldo
    self.agencia = agencia

conta_corrente = Conta_Corrente(4002, 8922, 1234)
print(f"Número: {conta_corrente.numero}, Saldo: R$ {conta_corrente.saldo:.2f}, Agência: {conta_corrente.agencia}")