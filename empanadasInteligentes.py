
eleccion= 0 

empanada = {'Nombre': None, 'Ingredientes': [], 'Precio Fabricacion': None, 'Precio Venta' : None}

while eleccion != 3:

    print("***Empanadas Inteligentes***")
    print("***************")
    print("1. Agregar Empanada")
    print("2. Mostrar Empanada")
    print("3. SALIR")

    eleccion= int(input('Digite la opcion del Menu: '))

    if eleccion == 1: 

        nombre = input('Digite el nombre de la empanada: ')
        
        ingredientes=[]

        for i in range(0,3,1):
            ingrediente = input(f'Ingrese el ingrediente numero {i+1}: ')

            ingredientes.append(ingrediente)

        precioFabricacion = float(input('Digite el precio de fabricacion: '))

        precioVenta  = float(input('Digite el precio de Venta: '))

        empanada['Nombre']= nombre

        empanada['Ingredientes'] = ingredientes

        empanada['Precio Fabricacion']= precioFabricacion

        empanada['Precio Venta']= precioVenta
        print('Empanada guardada exitosamente')

    elif eleccion == 2:

        for key, value in empanada.items():
            print(f'{key}: {value}')
    elif eleccion== 3:

        print('Gracias por usar el Menu de empanadas')
        break
    else: 
        print("Digite una opcion correcta ")
else: 
    print('Bye') 

