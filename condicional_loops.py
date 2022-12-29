#Condicional e Loops

print("Digite o seu nome")
nome = input()

print("Digite sua idade")
idade = input()

if int(idade) > 18:
    print("Maior de idade")
else:
    print("menor de idade")

print("Digite M para masculino, F para feminino, X para outros")
sexo = input()

if sexo == 'M':
    print("Masculino")
elif sexo == 'F':
    print("Feminino")
else:
    print("Outros")

print("Digite um numero para executarmos a tabuada")
numero = input()
numero = int(numero)
tabuada = range(0,11) # O for trabalha em array. Transforma um range de 1 a 10

print(f"Olá,{nome}. Segue abaixo o Fatorial do número que deseja:")

for i in tabuada:
    print(numero*i)

print("Veja as letras do seu nome")
for letra in nome:
    print(letra)

print("FIM")