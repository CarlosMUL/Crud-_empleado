import os
import json
os.system("cls")

def cargar_json(url_archivo):
    with open(url_archivo, 'r') as archivo:
        return json.load(archivo)
    

def menu_general():
    os.system("cls")
    print("1.- crear empleado")
    print("2.- actualizar empleado")
    print("3.- eliminar empleado")
    print("4.- listar empleado")
    print("5.- salir")


def seleccionar_opcion(max_opcion):
    opcion = 0
    while True:
        try:
            opcion = int(input("selecciones una opcion >>"))
        except:
            pass
        if opcion < 1 or opcion > max_opcion:
            input("opcion invalida intente nuevamente >>")
        else:
            return opcion

def iniciar_programa():
    while True:
        menu_general()
        opcion= seleccionar_opcion()

        if opcion == 1:
            print("1.- crear empleado")
        elif opcion == 2:
            print("2.- actualizar empleado")
        elif opcion == 3:
            print("3.- eliminar empleado")
        elif opcion == 4:
                empleados = cargar_json('empleados.json')
                print(empleados)
        elif opcion == 5:
              print("5.- salir")


iniciar_programa()