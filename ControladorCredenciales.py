# Imports
import json


# Variables Globales

# Funciones
def openCredenciales():
    with open('credenciales.json') as file:
        return json.load(file)


def saveCredenciales(data):
    with open('./credenciales.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


def newUser():
    name = input('Ingrese el nombre del nuevo usuario: ')
    users = openCredenciales()

    for i in users["usuarios"]:
        if i['usuario'] == name:
            print(f'El nombre: {name} ya esta registrado.')
            break
    else:
        newUsuario = {
            "usuario": name,
            "data": {
                "notion": [

                ]
            }
        }
        users["usuarios"].append(newUsuario)
        saveCredenciales(users)


def deleteUser():
    users = openCredenciales()

    for x, i in enumerate(users["usuarios"]):
        print(f'{x + 1}) {i["usuario"]}')
    user = int(input('Seleccione un el usuario a eliminar: ')) - 1

    if len(users['usuarios']) > user:
        users['usuarios'].pop(user)
        saveCredenciales(users)
        print(f'El usuario ha sido eliminado correctamente')
    else:
        print(f'Ha ingresado una opcion no valida o inexistente. Intente nuevamente.')

def modifyUser():
    users = openCredenciales()

    for x, i in enumerate(users["usuarios"]):
        print(f'{x}) {i["usuario"]}')
    user = int(input('Seleccione un el usuario a modificar: ')) - 1

    print('''
                NOTION
                1) Agregar Notion
                2) Eliminar Notion
                2) Modificar Notion
                4) Agregar Database
                5) Eliminar Database
                6) Modificar Database
                0) Regresar
            ''')
    opcionApp = input('Seleccione la aplicacion a modificar: ')

    if opcionApp == '1':
        while True:
            nombreNotion = input('Ingrese el nombre del Notion')
            existe = True
            for i in users["usuarios"]:
                if i['usuario'] == nombreNotion:
                    existe = False
                    print(f'El nombre: {nombreNotion} ya esta registrado. Intente nuevamente')
                    break

            if existe:
                token = input('Ingrese el token del Notion')

                newNotion = {
                    "nombreNotion": nombreNotion,
                    "token": token,
                    "databasesIds": [

                    ]
                }

                users['usuarios'][user]['data']['notion'].append(newNotion)
                saveCredenciales(users)
                break

    elif opcionApp == '2':
        for x, i in enumerate(users["usuarios"][user]['data']['notion']):
            print(f'{x}) {i["nombreNotion"]}')
        delNotion = int(input('Seleccione un el usuario a modificar: ')) - 1

        if len(users["usuarios"][user]['data']['notion']) <= delNotion:
            users['usuarios'][user]['data']['notion'].pop(delNotion)
            saveCredenciales(users)
            print('El Notion ha sido eliminado')

        else:
            print(f'Ha ingresado una opcion no valida o inexistente. Intente nuevamente.')


    elif opcionApp == '3':
        pass

    elif opcionApp == '4':
        pass
    elif opcionApp == '5':
        pass
    elif opcionApp == '6':
        pass
    elif opcionApp == '0':
        pass
