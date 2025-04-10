class Aluno:
  def __init__(self, nome, idade, matricula):
    self.nome = nome
    self.idade = idade
    self.matricula = matricula
  
aluno = Aluno("Gustavo", 19, 20242370003)
print(f"Nome: {aluno.nome}, Idade: {aluno.idade}, Matrícula: {aluno.matricula}")