def menor(n1, n2, n3) -> int:
    if n1 > n2:
        return n2
    elif n2 > n3:
        return n3
    else:
        return n1

def fatorial(n) -> int:
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    return fatorial

def vertical(texto):
    for char in texto:
        print(char)