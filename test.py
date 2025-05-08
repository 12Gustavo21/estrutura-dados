import functions as fc

print("MENOR")
print(fc.menor(1, 1, 3)) # 1
print(fc.menor(6, 6, 3)) # 3
print(fc.menor(6, 9, 9)) # 6
print(fc.menor(6, 2, 2)) # 2
print(fc.menor(9, 9, 9), "\n") # 9

print("FATORIAL")
print(fc.fatorial(3)) # 6
print(fc.fatorial(8)) # 40.320
print(fc.fatorial(9)) # 362.880
print(fc.fatorial(5), "\n") # 120

print("VERTICAL")
fc.vertical("abc")
print()
fc.vertical("oie")
print()
fc.vertical("xero")