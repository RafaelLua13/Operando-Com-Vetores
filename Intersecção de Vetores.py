# Encontrar mesmos valores em dois vetores

# Nome do projeto: Intersecção de Vetores 
# Linguagem: Python
# Utilizações: Variáveis, Repetições e Vetores
# Autor: Rafael Lua - rafaellua13

vetorA = [1,2,3,4,5]
vetorB = [4,5,6,7,8]
vetorC = [""] * (len(vetorA) + len(vetorB))

 
for i in range(len(vetorA)):
  for p in range(len(vetorB)):
     if vetorA[i] == vetorB[p]:
       vetorC[p] = vetorA[i]


for q in range(len(vetorC)):
  print(vetorC[q], end = " ")

print()
print()


       
