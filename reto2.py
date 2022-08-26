numero=int(input("Digite un numero entero: "))
modulo= numero%5

#Condicional simple en python
#hola

if(modulo==0):
    print(f'El numero {numero} es multiplo de 5')
else:
    print(f'El numero {numero} no es multiplo de 5, su residuo es: {modulo}')
print("fin del programa")