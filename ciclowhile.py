## ciclo mientras (while) 
## declarar una variable centinela o de contrl para evualuar la ejecucion de mi ciclo 
## en el conteo siempre se inicia desde 0 

i=0
##Menu de opciones

print("***MENU***")
print("1.Saludar")
print("2.Despedir ")
print("3.Quien gano el clasico ")
print("4.Esta lloviendo en medallo")
print("5. Salir")



while(i!=5):
    i=int(input("Digite  una opcion del menu "))

    if(i==1):
        print("Hola como estas ")
    elif(i==2):
            print("Chaoo ")
    elif(i==3):
        print("Ganador el rojo")   
    elif(i==4):
        print("no llueve en medello")
    elif(i==5):
        break
    else: 
        print("Digita una opcion valida")
       




