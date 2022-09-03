
eleccion= 0 

empanadas=[]

while eleccion != 3:

    print("***Empanadas Inteligentes***")
    print("***************")
    print("1. Agregar Empanada")
    print("2. Mostrar Empanada")
    print("3. SALIR")

    empanada = {}

    eleccion= int(input('Digite la opcion del Menu: '))

    if eleccion == 1: 

        nombre = input('Digite el nombre de la empanada: ')
        
        ingredientes=[]

        for i in range(3):
            ingrediente = input(f'Ingrese el ingrediente numero {i+1}: ')

            ingredientes.append(ingrediente)

        precioFabricacion = float(input('Digite el precio de fabricacion: '))

        precioVenta  = float(input('Digite el precio de Venta: '))

        empanada['Nombre']= nombre

        empanada['Ingredientes'] = ingredientes

        empanada['Precio Fabricacion']= precioFabricacion

        empanada['Precio Venta']= precioVenta
        print('Empanada guardada exitosamente')

        empanadas.append(empanada)

    elif eleccion == 2:

        print(empanadas)
    elif eleccion== 3:

        print('Gracias por usar el Menu de empanadas')
        break
    else: 
        print("Digite una opcion correcta ")
else: 
    print('Bye') 

