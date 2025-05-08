class Pilha:
    def __init__(self):
        self.__itens = []

    def vazia(self):
        return len(self.__itens) == 0

    def topo(self):
        if self.vazia():
            return None
        return self.__itens[-1]

    def empilhar(self, item):
        return self.__itens.append(item)

    def desempilhar(self):
        if self.vazia():
            return None
        return self.__itens.pop()

    def __str__(self):
        return self.__itens.__str__()


p = Pilha()
while True:
    print("\nEDITOR DE PILHA")
    print("[1] EMPILHAR")
    print("[2] DESEMPILHAR")
    print("[3] EXIBIR ELEMENTO DO TOPO")
    print("[4] EXIBIR A PILHA")
    print("[5] TAMANHO DA PILHA")
    print("[6] ESVAZIAR A PILHA")
    print("[0] SAIR")

    opcao = int(input("\nDIGITE SUA OPÇÃO: "))

    if opcao <= 0 or opcao > 6:
        print("\nSaindo do editor...")
        break
    elif opcao == 1:
        item = input("\nDigite o item a ser empilhado: ")
        p.empilhar(item)
        print(f"\nItem {item} empilhado")
    elif opcao == 2:
        removido = p.desempilhar()
        if removido is None:
            print("\nPilha vazia")
        else:
            print(f"\n{removido} removido")
    elif opcao == 3:
        topo = p.topo()
        if topo is None:
            print("\nPilha vazia")
        else:
            print(f"\nO elemento do topo é: {topo}")
    elif opcao == 4:
        print("Pilha: ", p)
    elif opcao == 5:
        cont = 0
        pt = []  # Lista temporária

        while not p.vazia():
            item = p.desempilhar()
            pt.append(item)
            cont += 1

        for item in reversed(pt):
            p.empilhar(item)

        print(f"\nTamanho da pilha: {cont}")
    elif opcao == 6:
        while not p.vazia():
            p.desempilhar()
        print("\nPilha esvaziada")