from correntista import Correntista

c = Correntista("Elias","08169401933", 500.0)
print(c)

print(c.nome())
print(c.saldo())
print(c.depositar(0))
print(c.depositar(50.0))
print(c.sacar(-600.0))
print(c.sacar(600.0))
print(c.sacar(399.76))
print(c.sacar("a"))
for hist in c:
    print(hist)