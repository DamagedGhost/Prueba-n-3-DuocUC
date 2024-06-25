
#! Calcular automáticamente:
   #! Descuento de Salud (7% del Sueldo Bruto).
   #! Descuento de AFP (10% del Sueldo Bruto).
   #! Sueldo Líquido (Sueldo Bruto - Descuentos).
#! Almacenar estos valores en una matriz para su posterior manejo.

#! Mostrar en pantalla la información de todos los trabajadores registrados, incluyendo Nombre y Apellido, Cargo, Sueldo Bruto, Descuento de Salud, Descuento de AFP y Sueldo Líquido.
#! Imprimir Planilla de Sueldos por Cargo

#! Mostrar en pantalla la información de los trabajadores que tienen ese cargo, incluyendo Nombre y Apellido, Sueldo Bruto, Descuento de Salud, Descuento de AFP y Sueldo Líquido.

#! Instrucciones Adicionales:

#! Implementa cada una de las opciones del menú como funciones separadas.

#! Asegúrate de validar la entrada de datos para garantizar la correcta operación de la aplicación:

#! Capturar y manejar excepciones inesperadas para evitar que el programa se detenga.
#! Los cálculos de descuentos deben ser precisos y mostrar el sueldo líquido correctamente.
#! Implementa la funcionalidad de guardar y cargar la matriz de trabajadores desde un archivo (por ejemplo, CSV) cada vez que inicie el programa.
#! Cada vez que se registre un nuevo trabajador, actualiza el archivo de almacenamiento.

#importamos librerias requeridas para el funcionamiento del programa
import json
import os
import time

#asignamos variables (buenas practicas)
key = 0
search_id = 0
nombre = ''
cargo = ''
cargo_lista = ['Mesero', 'Cocinero', 'Cajero']
sueldo_liquido = 0          #* bruto - dctos
sueldo_bruto = 0            
dcto_salud = 0.93
dcto_AFP = 0.90

#creamos un diccionario para su posterior manejo
diccionario_trabajador = {'nombre': 'example example', 'cargo':'example', 'sueldo_bruto':0}

#validamos que el archivo exista, de no ser asi, crea uno nuevo
if not os.path.exists('trabajadores.json'):
    with open('trabajadores.json', 'w') as trabajadores_json:
        json.dump({'next_id':0,'trabajadores':{}},trabajadores_json)

with open('trabajadores.json', 'r') as trabajadores_json:
    datos = json.load(trabajadores_json)




#funcion de agregar nuevos trabajadoes              #*FUNCIONA AL 100%
def agregar_personas():
    try:
        while True:         #! FALTA VALIDAR
            print('MENU AGREGAR PERSONAS\n\nElija uno de los cargos\n1) Mesero\n2) Cocinero\n3) Cajero\n\n')
            key = input('Opcion: ')
            while not key.isnumeric():
                key = input('Ingrese una opcion valida: ')
            key = int(key)

            if key == 1:
                cargo = 'mesero'
                break
            elif key == 2:
                cargo = 'cocinero'
                break
            elif key == 3:
                cargo = 'cajero'
                break
            else:
                print('\nPor favor, escoja una opcion valida\n')

        nombre = input('Escriba el nombre y apellido: ')
        sueldo_bruto = input('Escriba el sueldo bruto del trabajador: ')

        diccionario_trabajador = {'nombre': nombre, 'cargo': cargo, 'sueldo_bruto':sueldo_bruto}

        new_id_user = datos['next_id']
        datos['next_id'] +=1

        datos['trabajadores'][new_id_user] = diccionario_trabajador                         

        with open('trabajadores.json', 'w') as trabajadores_json:
            json.dump(datos,trabajadores_json,indent=4)
            print(f'usuario {nombre} agregado exitosamente')
    except: Exception
    print(f'error al agregar persona\n{Exception}')    




#funcion para listar al detalle todas las personas #!FALTA MOSTRAR DETALLES
def listar_personas():              #*FUNCIONA AL 100%
    try:        
        for user_id in datos['trabajadores'].items():
            print(f' {user_id}')            # - nombre{user_id['nombre']} - cargo{data['cargo']} - sueldo bruto{data['sueldo_bruto']}')
    except:Exception
    print(f'error al listar personas\n{Exception}')




#funcion para modificar personas #!NO FUNCIONA
def modificar_personas():
    try:
        print('MENU MODIFICAR PERSONAS\n\n1) Editar personas\n2) Eliminar personas\n\n')
        key = input('Opcion: ')
        while not key.isnumeric():
            key = input('Ingrese una opcion valida: ')
        key = int(key)

        if key == 1:
            search_id = input('Ingrese una id para buscar')
            while not search_id.isnumeric():
                search_id = input('ingrese una ID valida')
            search_id = str(search_id)              #? se transforma a str, ya que de esta forma se podra comparar con el archivo json

            if search_id in trabajadores_json['trabajadores']:
                # print(f'datos actuales del trabajador\n{datos['trabajadores'][search_id]}')

                while True:         #! FALTA VALIDAR
                    print('MENU AGREGAR PERSONAS\n\nElija uno de los cargos\n1) Mesero\n2) Cocinero\n3) Cajero\n\n')
                    key = input('Opcion: ')
                    while not key.isnumeric():
                        key = input('Ingrese una opcion valida: ')
                    key = int(key)

                    if key == 1:
                        cargo = 'mesero'
                        break
                    elif key == 2:
                        cargo = 'cocinero'
                        break
                    elif key == 3:
                        cargo = 'cajero'
                        break
                    else:
                        print('\nPor favor, escoja una opcion valida\n')
                nombre = input('ingrese nuevo nombre [dejar en blanco para mantener]: ')
                sueldo_bruto = input('ingrese nuevo sueldo bruto (calculos dcto se haran despues de guardar) [dejar en blanco para mantener]: ')
                diccionario_trabajador = {'nombre': nombre, 'cargo': cargo, 'sueldo_bruto':sueldo_bruto}
                datos['trabajadores'][search_id] = diccionario_trabajador
    except: Exception
    print(f'error al modificar persona\n{Exception}')



#FUNCION PARA CALCLAR SUELDOS DE TRABAJADORES, SEGUN ID
def calcular_detalle():             #!INCOMPLETO
    try:
        search_id = input('Ingrese una id para buscar')
        while not search_id.isnumeric():
            search_id = input('ingrese una ID valida')
        search_id = str(search_id)

        if search_id in datos['trabajadores']:
            print('ye')
        else:
            print('no se encontraron datos')
    except:Exception
    print(f'error al calcular detalle de sueldos\n{Exception}')



while True:
    try:
        print('MENU PRINCIPAL\n\n1) Agregar personas\n2) Listar personas\n3) Modificar personas\n4) Mostrar detalle sueldos\n\n')
        key = input('Opcion: ')
        while not key.isnumeric():
            key = input('Ingrese una opcion valida: ')
        key = int(key)

        if key == 1:
            agregar_personas()
        elif key == 2:
            listar_personas()
        elif key == 3:
            modificar_personas()
        elif key == 4:
            calcular_detalle()
        elif key == 9:
            print('gracias por usar el programa..')
            break
        else:
            print('\nIngrese una opcion valida')
    except: Exception
    print(f'error al ejecutar el programa..\n{Exception}')