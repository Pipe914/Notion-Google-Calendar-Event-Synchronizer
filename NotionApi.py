'''Imports necesarios'''
import requests
import json
from datetime import datetime

def readDatabase(databaseId, headers, opcion):
    readUrl = f'https://api.notion.com/v1/databases/{databaseId}/query'
    date = datetime.today().strftime('%Y-%m-%d')
    print(date)
    if opcion == '1':
        filtroOpcion1 = {
            'filter': {
                'and': [
                    {
                        'property': 'Fecha Creado',
                        'date': {
                            'after': f'{date}T00:00:00'
                        }
                    },
                    {
                        'property': 'Calendar ID',
                        'text': {
                            'is_empty': True
                        }
                    },
                    {
                        'property': 'Status',
                        'select': {
                            'equals': 'Activo'
                        }
                    }

                ]
            }
        }
        data = json.dumps(filtroOpcion1)
        res = requests.request('POST', readUrl, headers=headers, data=data)
        if res.status_code == 200:
            data = res.json()
            with open('./dataCreados.json', 'w', encoding='utf8') as f:
                json.dump(data, f, ensure_ascii=False)
            print('Operacion completada', res, data)
        else:
            print(f'Error: {res.status_code}. Detalles: {res.text}')

    elif opcion == '2':
        filtroOpcion2 = {
            'filter': {
                'and': [
                    {
                        'property': 'Fecha Editado',
                        'date': {
                            'after': f'{date}T00:00:00'
                        }
                    },
                    {
                        'property': 'Calendar ID',
                        'text': {
                            'is_not_empty': True
                        }
                    },
                    {
                        'property': 'Status',
                        'select': {
                            'equals': 'Activo'
                        }
                    }

                ]
            }
        }
        data = json.dumps(filtroOpcion2)
        res = requests.request('POST', readUrl, headers=headers, data=data)
        if res.status_code == 200:
            data = res.json()
            with open('./dataActualizados.json', 'w', encoding='utf8') as f:
                json.dump(data, f, ensure_ascii=False)
            print('Operacion completada', res, data)
        else:
            print(f'Error: {res.status_code}. Detalles: {res.text}')


def readTodo(databaseId, headers):
    readUrl = f'https://api.notion.com/v1/databases/{databaseId}/query'

    res = requests.request('POST', readUrl, headers=headers)
    if res.status_code == 200:
        data = res.json()
        with open('./database.json', 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)
        print('Operacion completada', res, data)
    else:
        print(f'Error: {res.status_code}. Detalles: {res.text}')


def createPageAllDay(databaseId, headers, data):
    createUrl = 'https://api.notion.com/v1/pages'

    newPageData = {
        'parent': {'database_id': databaseId},
        'properties': {
            'Descripcion': {
                'title': [
                    {
                        'text': {
                            'content': data[0]
                        }
                    }
                ]
            },
            'Fecha': {
                'date': {
                    'start': data[1]
                }
            },
            'Materia': {
                'select': {
                    'name': data[2]
                }
            },
            'Estado': {
                'checkbox': data[3]
            },
            'Info': {
                'rich_text': [
                    {
                        'text': {
                            'content': data[4]
                        }
                    }
                ]
            },
            'All Day': {
                'select': {
                    'name': data[5]
                }
            },
            'Status': {
                'select': {
                    'name': data[6]
                }
            },
            'Info': {
                'rich_text': [
                    {
                        'type': 'text',
                        'text': {
                            'content': data[7]
                        }
                    }
                ]
            }
        }
    }

    data = json.dumps(newPageData)
    res = requests.request('POST', createUrl, headers=headers, data=data)
    if res.status_code == 200:
        print('Operacion completada')
    else:
        print(f'Error: {res.status_code}. Detalles: {res.text}')


def createPageAllDay(databaseId, headers, data):
    createUrl = 'https://api.notion.com/v1/pages'

    newPageData = {
        'parent': {'database_id': databaseId},
        'properties': {
            'Descripcion': {
                'title': [
                    {
                        'text': {
                            'content': data[0]
                        }
                    }
                ]
            },
            'Fecha': {
                'date': {
                    'start': data[1]
                }
            },
            'Materia': {
                'select': {
                    'name': data[2]
                }
            },
            'Estado': {
                'checkbox': data[3]
            },
            'Info': {
                'rich_text': [
                    {
                        'text': {
                            'content': data[4]
                        }
                    }
                ]
            },
            'All Day': {
                'select': {
                    'name': data[5]
                }
            },
            'Status': {
                'select': {
                    'name': data[6]
                }
            },
            'Info': {
                'rich_text': [
                    {
                        'type': 'text',
                        'text': {
                            'content': data[7]
                        }
                    }
                ]
            }
        }
    }

    data = json.dumps(newPageData)
    res = requests.request('POST', createUrl, headers=headers, data=data)
    if res.status_code == 200:
        print('Operacion completada')
    else:
        print(f'Error: {res.status_code}. Detalles: {res.text}')


def updatePage(pageId, headers, data):
    updateUrl = f'https://api.notion.com/v1/pages/{pageId}'

    updateData = {
        'properties': {
            'Info': {
                'rich_text': [
                    {
                        'text': {
                            'content': 'Otra prueba por aqui'
                        }
                    }
                ]
            },
        }
    }

    data = json.dumps(updateData)
    res = requests.request('PATCH', updateUrl, headers=headers, data=data)
    if res.status_code == 200:
        print('Operacion completada')
    else:
        print(f'Error: {res.status_code}. Detalles: {res.text}')

def addIdCalendar(pageId, headers, data):
    addCalendarUrl = f'https://api.notion.com/v1/pages/{pageId}'

    addIdCalendarQuery= {
        'properties': {
            'Calendar ID': {
                'rich_text': [
                    {
                        'text': {
                            'content': data
                        }
                    }
                ]
            },
        }
    }
    data = json.dumps(addIdCalendarQuery)
    res = requests.request('PATCH', addCalendarUrl, headers=headers, data=data)
    if res.status_code == 200:
        print('Operacion completada')
    else:
        print(f'Error: {res.status_code}. Detalles: {res.text}')

def queryDatabase(databaseId, headers):
    queryUrl = f'https://api.notion.com/v1/databases/{databaseId}/query'

    queryData = {
        'filter': {
            'and': [
                {
                    'property': 'Fecha Creado',
                    'date': {
                        'after': '2021-12-17'
                    }

                },
                {
                    'property': 'Status',
                    'select': {
                        'equals': 'Activo'
                    }
                }
            ]
        }
    }

    data = json.dumps(queryData)
    res = requests.request('POST', queryUrl, headers=headers, data=data)
    if res.status_code == 200:
        dataResponse = res.json()
        with open('./query.json', 'w', encoding='utf8') as f:
            json.dump(dataResponse, f, ensure_ascii=False)
        print('Operacion completada')
    else:
        print(f'Error: {res.status_code}. Detalles: {res.text}')


# readDatabase(databaseId, headersRead)