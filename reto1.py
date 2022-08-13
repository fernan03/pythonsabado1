numero=int(input("Digite un numero entero: "))
modulo= numero%3

#Condicional simple en python

if(modulo==0):
    print(f'El numero {numero} es multiplo de 3')
else:
    print(f'El numero {numero} no es multiplo de 3, su residuo es: {modulo}')
print("fin del programa")

