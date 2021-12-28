from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
calendarId = 'ip3cmampqo8k8euu9mp28sfu3s@group.calendar.google.com'

# Crear un evento
def crearEventoHora(data):
    timeAdjustment = +5
    event_request_body = {
        'summary': data[0],
        'description': data[1],
        'start': {
            'dateTime': convert_to_RFC_datetime(int(data[2][0]), int(data[2][1]), int(data[2][2]), int(data[2][3])+timeAdjustment, int(data[2][4])),
            'timeZone': 'America/Bogota'
        },
        'end': {
            'dateTime': convert_to_RFC_datetime(int(data[3][0]), int(data[3][1]), int(data[3][2]), int(data[3][3])+timeAdjustment, int(data[3][4])),
            'timeZone': 'America/Bogota'
        },
        'visibility': 'private'
    }
    return service.events().insert(calendarId=calendarId, body=event_request_body).execute()

def crearEventoFullDia(data):
    event_request_body = {
        'summary': data[0],
        'description': data[1],
        'start': {
            'date': f'{data[2][0]}-{data[2][1]}-{data[2][2]}',
            'timeZone': 'America/Bogota'
        },
        'end': {
            'date': f'{data[2][0]}-{data[2][1]}-{data[2][2]}',
            'timeZone': 'America/Bogota'
        },
        'visibility': 'private'
    }
    return service.events().insert(calendarId=calendarId, body=event_request_body).execute()

def actualizarEventoFullDia(data):
    event_request_body = {
        'summary': data[0],
        'description': data[1],
        'start': {
            'date': f'{data[2][0]}-{data[2][1]}-{data[2][2]}',
            'timeZone': 'America/Bogota'
        },
        'end': {
            'date': f'{data[2][0]}-{data[2][1]}-{data[2][2]}',
            'timeZone': 'America/Bogota'
        },
        'visibility': 'private'
    }
    return service.events().update(calendarId=calendarId, eventId=data[3], body=event_request_body).execute()

def actualizarEventoHora(data):
    timeAdjustment = +5
    event_request_body = {
        'summary': data[0],
        'description': data[1],
        'start': {
            'dateTime': convert_to_RFC_datetime(int(data[2][0]), int(data[2][1]), int(data[2][2]), int(data[2][3])+timeAdjustment, int(data[2][4])),
            'timeZone': 'America/Bogota'
        },
        'end': {
            'dateTime': convert_to_RFC_datetime(int(data[3][0]), int(data[3][1]), int(data[3][2]), int(data[3][3])+timeAdjustment, int(data[3][4])),
            'timeZone': 'America/Bogota'
        },
        'visibility': 'private'
    }
    return service.events().update(calendarId=calendarId, eventId=data[4], body=event_request_body).execute()

#Actualizar un evento: Enviar un nuevo envet body pero a diferente service
#response = service.events().update(calendarId = calendarId, eventId = eventId, body = body).execute()