# Intercalar dois vetores sem comandos lista

# Nome do projeto: Intercalar Vetores
# Linguagem: Python
# Utilizações: Variáveis, Repetições e Vetores
# Autor: Rafael Lua - rafaellua13

A = [1,3,6,7,8,9]
B = [2,4,5,10]

a = 0
b = 0
C = [0] * (len(A) + len((B))) 

for x in range(len(C)):
  if A[a] < B[b]:
    C[x] = A[a]

    if a + 1 < len(A):
      a += 1

    else: 

      A[a] = B[b] + A[a] 

  else:
    C[x] = B[b]

    if b + 1 < len(B):
      b += 1

    else: 
      B[b] = A[a] + B[b]

print(C)

