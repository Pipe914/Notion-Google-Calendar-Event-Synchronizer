# Imports
import Calendar
import ControladorCredenciales as credenciales
import NotionApi as notion
import json

# Variables globales

'''Headers para enviar peticiones'''

def crearHeaders(token):
    global headers
    headers = {
        'read': {
            'Authorization': f'Bearer {token}',
            'Notion-Version': '2021-08-16'
        },
        'create': {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Notion-Version': '2021-08-16'
        },
        'update': {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Notion-Version': '2021-08-16'
        }
    }


# Funciones de herramientas
def formatoFecha(fecha, opcion):
    fechaCompleta = []
    if opcion == 1:
        dia = fecha.split('T')
        dia = dia[0].split('-')
        for i in dia:
            fechaCompleta.append(i)
    elif opcion == 2:
        dia = fecha.split('T')
        hora = dia[1].split('-')
        dia = dia[0].split('-')
        hora = hora[0].split(':')
        for i in dia:
            fechaCompleta.append(i)
        for i in hora:
            fechaCompleta.append(i)
        fechaCompleta.pop()
    return fechaCompleta


# Declaracion de funciones
def seleccionCredenciales():
    usuarios = credenciales.openCredenciales()

    print('USUARIOS:')
    for i, nombre in enumerate(usuarios['usuarios']):
        print(f'{i + 1}) {usuarios["usuarios"][i]["usuario"]}')
    usuario = int(input('Seleccione el usuario: '))-1

    print('NOTION:' )
    for i, database in enumerate(usuarios['usuarios'][usuario]['data']['notion']):
        print(f'{i + 1} ) {usuarios["usuarios"][usuario]["data"]["notion"][i]["nombreNotion"]}')
    notion = int(input('Seleccione el Notion: ')) - 1

    print('DATABASE:')
    for i, database in enumerate(usuarios['usuarios'][usuario]['data']['notion'][notion]['databaseIds']):
        print(f'{i + 1} ) {usuarios["usuarios"][usuario]["data"]["notion"][notion]["databaseIds"][i]["nombreDB"]}')
    database = int(input('Seleccione la database: ')) - 1

    token = usuarios['usuarios'][usuario]['data']['notion'][notion]['token']
    databaseId = usuarios['usuarios'][usuario]['data']['notion'][notion]['databaseIds'][database]['databaseId']

    return [token, databaseId]

def verEventosCreados(token, databaseId):
    crearHeaders(token)
    notion.readDatabase(databaseId, headers.get('create'), '1')


def verEventosActualizados(token, databaseId):
    crearHeaders(token)
    notion.readDatabase(databaseId, headers.get('create'), '2')


def verEventos(token, databaseId):
    crearHeaders(token)
    notion.readTodo(databaseId, headers.get('create'))


def pushEvetosCreados(token, database):
    verEventosCreados(token, database)

    with open('dataCreados.json') as file:
        data = json.load(file)

    for i in range(len(data['results'])):
        if data['results'][i]['properties']['All Day']['select']['name'] == 'true':
            nombre = data['results'][i]['properties']['Descripcion']['title'][0]['text']['content']
            info = data['results'][i]['properties']['Info']['rich_text'][0]['text']['content']
            fecha = formatoFecha(data['results'][i]['properties']['Fecha']['date']['start'], 1)
            pageId = data['results'][i]['id']
            aux = []
            aux.append(nombre)
            aux.append(info)
            aux.append(fecha)
            response = Calendar.crearEventoFullDia(aux)
            notion.addIdCalendar(pageId, headers.get('create'), response['id'])
            print('El evento se ha creado correctamente')

        elif data['results'][i]['properties']['All Day']['select']['name'] == 'false':
            nombre = data['results'][i]['properties']['Descripcion']['title'][0]['text']['content']
            info = data['results'][i]['properties']['Info']['rich_text'][0]['text']['content']
            fechaInicio = formatoFecha(data['results'][i]['properties']['Fecha']['date']['start'], 2)
            fechaFinal = formatoFecha(data['results'][i]['properties']['Fecha']['date']['end'], 2)
            pageId = data['results'][i]['id']
            aux = []
            aux.append(nombre)
            aux.append(info)
            aux.append(fechaInicio)
            aux.append(fechaFinal)
            response = Calendar.crearEventoHora(aux)
            notion.addIdCalendar(pageId, headers.get('create'), response['id'])
            print('El eventos se ha creado correctamente')


def pushEventosActualizados(token, database):
    verEventosActualizados(token, database)

    with open('dataActualizados.json') as file:
        data = json.load(file)

    for i in range(len(data['results'])):
        if data['results'][i]['properties']['All Day']['select']['name'] == 'true':
            nombre = data['results'][i]['properties']['Descripcion']['title'][0]['text']['content']
            info = data['results'][i]['properties']['Info']['rich_text'][0]['text']['content']
            fecha = formatoFecha(data['results'][i]['properties']['Fecha']['date']['start'], 1)
            pageId = data['results'][i]['id']
            eventId = data['results'][i]['properties']['Calendar ID']['rich_text'][0]['text']['content']
            aux = []
            aux.append(nombre)
            aux.append(info)
            aux.append(fecha)
            aux.append(eventId)
            response = Calendar.actualizarEventoFullDia(aux)
            notion.addIdCalendar(pageId, headers.get('create'), response['id'])
            print('El evento se ha creado correctamente')

        elif data['results'][i]['properties']['All Day']['select']['name'] == 'false':
            nombre = data['results'][i]['properties']['Descripcion']['title'][0]['text']['content']
            info = data['results'][i]['properties']['Info']['rich_text'][0]['text']['content']
            fechaInicio = formatoFecha(data['results'][i]['properties']['Fecha']['date']['start'], 2)
            fechaFinal = formatoFecha(data['results'][i]['properties']['Fecha']['date']['end'], 2)
            pageId = data['results'][i]['id']
            eventId = data['results'][i]['properties']['Calendar ID']['rich_text'][0]['text']['content']
            aux = []
            aux.append(nombre)
            aux.append(info)
            aux.append(fechaInicio)
            aux.append(fechaFinal)
            aux.append(eventId)
            response = Calendar.actualizarEventoHora(aux)
            notion.addIdCalendar(pageId, headers.get('create'), response['id'])
            print('El eventos se ha creado correctamente')
