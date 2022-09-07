## LOS DICCIONARIO SON VARIABLES ESPECIALES QUE ME PERMITEN ALMACENAR MULTIPLES DATOS 
## DE DIFERENTE "TIPO EN UNA SOLA VARIABLE"

## en un diccionario tengo atributos  
## la propiedad siempre va entre comillas simples
## para acceder a una propiedad-- ejemplo 

empleado={
    'nombre':"Juan",
    'cedula':1035833544, 
    'cargo':"analista de datos",
    'salario':8000000,
    'horasTrabajadas':40,
    'aplicaSubsidioTransporte':False,
    'deudas':[1500000,8000000]


}
#print(empleado)
#print(empleado['deudas'][1])


## RECORRIENDO UN DICCIONARIO F
## diccionario 2 observadores ( atributo - valor)
## siempre aclaramos quien observa y que se observa


for observadorAtributo,observadorValor in empleado.items():
    print(observadorAtributo)
    print(observadorValor)


