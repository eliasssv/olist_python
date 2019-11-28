letras = ['a','b','c','d','e','f','g']
print(letras)
letras[2:5] = ['C', 'D', 'E']
print(letras)
letras[2:5] = []
print(letras)
letras[2:2] = [1,2]
print(letras)
letras[:] = [] # se nao fizer com [:] a lista original permanece alocada
print(letras)

a = ['a','b','c']
n = [1,2,3]
x = [a,n]
print(x)
print(x[0])
print(x[0][1])
x[0][1] = 'www'
print(a)
print(x[0][1])