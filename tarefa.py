#1
indice = 13
soma = 0
k = 0
while k < indice:
    k = k + 1
    soma = soma + k
print(soma)

#2
inicio,proximo= 0,1
numero = int(input("Informe um número: "))
while inicio < numero:
    inicio,proximo = proximo, inicio + proximo

if inicio == numero:
    print("Percente à sequencia de Fibonacci.")
else: 
    print("Esse número não pertence à sequencia de Fibonaci.")

#3

faturamento = []
dias = int(input("quantos dias trabalhados teve o mes?"))
for x in range(0,dias):
    faturamento_dia = float(input("Qual foi o faturamento do dia? "))
    faturamento_dia.append(faturamento)
menor= min(faturamento)
maior= max(faturamento)

media = sum(faturamento) / len(faturamento)
cont = 0
for i in faturamento:
    if faturamento[i] > media:
        cont = cont+1
print(f"O maior valor do mes foi {maior} ")
print(f"O menor valor do mes foi {menor} ")
print(f"Em {cont} dias o faturamento foi maior que a média mensal")


#4
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
total = (sp + rj + mg + es + outros)

print(f"SP: {(sp / total) * 100:.2f}%")
print(f"RJ: {(rj / total) * 100:.2f}%")
print(f"MG: {(mg / total) * 100:.2f}%")
print(f"ES: {(es / total) * 100:.2f}%")
print(f"Outros: {(outros / total) * 100:.2f}%")

#5
palavra= input("Digite algo: ")
lista= list(palavra)
lista.reverse()
revertida= ''.join(lista)
print(revertida)

invertida = palavra[::-1]
print(invertida)
