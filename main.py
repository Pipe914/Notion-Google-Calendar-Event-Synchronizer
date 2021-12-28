# Imports necesarios
import ControladorCredenciales as credenciales
import Automatizador as auto

def menuRead():
    while True:
        print('''
            VER EVENTOS
            1. Creados
            2. Actualizados
            3. Todos
            0. Regresar
            ''')
        selection = input('Seleccione una opcion: ')
        if selection == '1':
            data = auto.seleccionCredenciales()
            auto.verEventosCreados(data[0], data[1])
        elif selection == '2':
            data = auto.seleccionCredenciales()
            auto.verEventosActualizados(data[0], data[1])
        elif selection == '3':
            data =auto.seleccionCredenciales()
            auto.verEventos(data[0], data[1])
        elif selection == '0':
            print('Adios')
            break
        else:
            print('Opcion erronea, intente nuevamente.')


def menuActualizar():
    while True:
        print('''
            PUSH EVENTOS
            1. Creados
            2. Actualizados
            0. Regresar
            ''')
        selection = input('Seleccione una opcion: ')
        if selection == '1':
            data = auto.seleccionCredenciales()
            auto.pushEvetosCreados(data[0], data[1])
        elif selection == '2':
            data = auto.seleccionCredenciales()
            auto.pushEventosActualizados(data[0], data[1])
        elif selection == '0':
            print('Adios')
            break
        else:
            print('Opcion erronea, intente nuevamente.')
def menuUsuarios():
    while True:
        print('''
            USUARIOS
            1. Agregar usuario
            2. Modificar usuario
            3. Eliminar usuario
            0. Regresar
            ''')
        selection = input('Seleccione una opcion: ')
        if selection == '1':
            credenciales.newUser()
        elif selection == '2':
            credenciales.modifyUser()
        elif selection == '3':
            credenciales.deleteUser()
        elif selection == '0':
            break
        else:
            print('Opcion erronea, intente nuevamente.')

def menuPrincipal():
    while True:
        print('''
            MENU PRINCIPAL
            1. Ver eventos
            2. Push eventos
            3. Usuarios
            0. Exit
            ''')

        selection = input('Seleccione una opcion: ')
        if selection == '1':
            menuRead()
        elif selection == '2':
            menuActualizar()
        elif selection == '3':
            menuUsuarios()
        elif selection == '0':
            print('Adios')
            break
        else:
            print('Opcion erronea, intente nuevamente.')

menuPrincipal()

