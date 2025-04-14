## Verifique se o número é primo.
## Aluno: João Pedro Moreira


## Função
n = int(input("Digite o seu número: "))

primo = 1

for i in range(2,n):
    print (i)
    if (n % i == 0):
        primo = 0

if (primo == 1):
    print ("O número é primo")
else:
    print ("O número não é primo")