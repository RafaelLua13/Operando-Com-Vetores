# Subtrair um vetor de outro sem usar comandos Lista

# Nome do projeto: Subtração de Vetores
# Linguagem: Python
# Utilizações: Variáveis, Repetições e Vetores
# Autor: Rafael Lua - rafaellua13

A = [1,2,3,4]

B = [2,3]

C = [""] * len(A)
for x in range(len(A)):
    existe = False
    for y in range(len(B)):
      if A[x] == B[y]:
        existe = True
        break
      else:
        existe = False
	 
    
    if existe == False:
	    C[x] = A[x]


for z in range(len(C)):
  if C[z] != "":
    print(C[z], end = " ")  # A - B



