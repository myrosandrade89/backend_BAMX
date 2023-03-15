from rest_framework import viewsets, permissions, status
from turnos.models import Turno
from turnos.serializers import TurnoSerializer
from rest_framework.response import Response
from link.models import Link
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from datetime import datetime
from pytz import timezone
import json

def write_google_sheets(id_comunidad, comunidad, turno):
    # define the scope
    scope = ['https://www.googleapis.com/auth/spreadsheets']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads("""
    
    """), scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)
    
    link = Link.objects.all().order_by('-fecha_creacion')[0].liga

    # get the instance of the Spreadsheet
    try:
        sheet = client.open_by_url(link)
    except UnboundLocalError:
        return Response({'detail': 'URL not accesible'}, status=status.HTTP_400_BAD_REQUEST)
    except gspread.exceptions.APIError:
        return Response({'detail': 'URL not accesible'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)

    worksheet = sheet.get_worksheet(0)

    id_comunidad_cell = worksheet.find('CLAVE/ID')
    comunidad_cell = worksheet.find('COMUNIDAD')
    hora_llegada_cell = worksheet.find('HORA\nENTRADA')
    turno_cell = worksheet.find('TURNO')

    try:
        header_row = Link.objects.all().order_by('-fecha_creacion')[0].fila_inicial
        id_comunidad_column = id_comunidad_cell.col
        comunidad_column = comunidad_cell.col
        hora_llegada_column = hora_llegada_cell.col
        turno_column = turno_cell.col
        
    except AttributeError:
        return Response({'detail': 'Error: A column was not found'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)


    write_row = header_row + turno
    above_row = write_row - 1 
    below_row = write_row + 1

    # Checking the above row is filled
    if None in (worksheet.cell(above_row, id_comunidad_column).value, worksheet.cell(above_row, comunidad_column).value, worksheet.cell(above_row, hora_llegada_column).value, worksheet.cell(above_row, turno_column).value):
        return Response({'detail': f'Please fill the row {above_row} of the file and try again'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Checking the actual row is not filled
    if (worksheet.cell(write_row, id_comunidad_column).value is not None or worksheet.cell(write_row, comunidad_column).value is not None or  worksheet.cell(write_row, hora_llegada_column).value is not None or worksheet.cell(write_row, turno_column).value is not None):
        return Response({'detail': f'The row {write_row} is already filled'}, status=status.HTTP_400_BAD_REQUEST)

    # Checking the following row is empty 
    if (worksheet.cell(below_row, id_comunidad_column).value is not None or worksheet.cell(below_row, comunidad_column).value is not None or worksheet.cell(below_row, hora_llegada_column).value is not None or worksheet.cell(below_row, turno_column).value is not None):
        return Response({'detail': f'The row {below_row} is already filled and it should not'}, status=status.HTTP_400_BAD_REQUEST)
        

    
    now_time = datetime.now(timezone('America/Mexico_City'))
    now_time = now_time.strftime('%I:%M %p')

    # Updating the file
    worksheet.update_cell(write_row, id_comunidad_column, id_comunidad)
    worksheet.update_cell(write_row, comunidad_column, comunidad)
    worksheet.update_cell(write_row, hora_llegada_column, now_time)
    worksheet.update_cell(write_row, turno_column, turno)

class TurnoViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows turnos to be viewed or edited.
  """
  queryset = Turno.objects.all().order_by('numero')
  serializer_class = TurnoSerializer
  permission_classes = [permissions.IsAuthenticated]

  def perform_create(self, serializer):
    comunidad = serializer.validated_data['comunidad']
    numero = serializer.validated_data['numero']
    write_google_sheets(comunidad.clave_sae, comunidad.nombre, numero)
    return super().perform_create(serializer)
