# Unir em um novo vetor os elementos de dois vetores


# Nome do projeto: União de Vetores 
# Linguagem: Python
# Utilizações: Variáveis, Repetições e Vetores
# Autor: Rafael Lua - rafaellua13


vetor1 = [1,2,3,4,5]
vetor2 = [4,5,6,7,8,9]
vetor3 = [""] * (len(vetor1) + len(vetor2))

for x in range(len(vetor1)):
  vetor3[x] = vetor1[x]



cont = len(vetor1) - 1



for z in range(len(vetor2)):
    
    for y in range(len(vetor1)):
      if vetor2[z] != vetor1[y]:
        existe = False
        
      else:
        existe = True
        break
    
    if existe == False:
      cont += 1
      vetor3[cont] = vetor2[z]

#print(vetor3)

for a in range(len(vetor3)):
  print(vetor3[a], end = " ")

print()

