numero1=int(input("Digite primer numero entero: "))
numero2=int(input("Digite segundo numero entero: "))

if(numero1 > numero2):
    print(f'El numero {numero1} es mayor que {numero2}')
elif(numero1 < numero2):
    print(f'El numero {numero2} es mayor que {numero1}')
elif(numero1 == numero2):
    print(f'El numero {numero1} es igual que {numero2}')
else:
    print(f'Digite valores validos')