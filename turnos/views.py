from rest_framework import viewsets, permissions
from turnos.models import Turno
from turnos.serializers import TurnoSerializer

from link.models import Link

from oauth2client.service_account import ServiceAccountCredentials
import gspread
from datetime import datetime
from pytz import timezone


def write_google_sheets(id_comunidad, comunidad, turno):
    # define the scope
    scope = ['https://www.googleapis.com/auth/spreadsheets']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('.\\secret_key.json', scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)
    
    link = Link.objects.all().order_by('-fecha_creacion')[0].liga

    # get the instance of the Spreadsheet
    try:
        sheet = client.open_by_url(link)
    except UnboundLocalError:
        print('URL not accesible')
        raise SystemExit
    except gspread.exceptions.APIError:
        print('URL not accesible')
        raise SystemExit
    except Exception as e:
        print(e)
        raise SystemExit

    worksheet = sheet.get_worksheet(0)

    id_comunidad_cell = worksheet.find('CLAVE/ID')
    comunidad_cell = worksheet.find('COMUNIDAD')
    hora_llegada_cell = worksheet.find('HORA\nENTRADA')
    turno_cell = worksheet.find('TURNO')

    try:
        header_row = id_comunidad_cell.row
        id_comunidad_column = id_comunidad_cell.col
        comunidad_column = comunidad_cell.col
        hora_llegada_column = hora_llegada_cell.col
        turno_column = turno_cell.col
        
    except AttributeError:
        print('Error: A column was not found')
        raise SystemExit
    except Exception as e:
        print(e)
        raise SystemExit

    write_row = header_row + turno
    above_row = write_row - 1 
    below_row = write_row + 1

    # Checking the above row is filled
    if None in (worksheet.cell(above_row, id_comunidad_column).value, worksheet.cell(above_row, comunidad_column).value, worksheet.cell(above_row, hora_llegada_column).value, worksheet.cell(above_row, turno_column).value):
        print(f'Please fill the row {above_row} of the file and try again')
        raise SystemExit
    
    # Checking the actual row is not filled
    if (worksheet.cell(write_row, id_comunidad_column).value is not None or worksheet.cell(write_row, comunidad_column).value is not None or  worksheet.cell(write_row, hora_llegada_column).value is not None or worksheet.cell(write_row, turno_column).value is not None):
        print(f'The row {write_row} is already filled')
        raise SystemExit

    # Checking the following row is empty 
    if (worksheet.cell(below_row, id_comunidad_column).value is not None or worksheet.cell(below_row, comunidad_column).value is not None or worksheet.cell(below_row, hora_llegada_column).value is not None or worksheet.cell(below_row, turno_column).value is not None):
        print(f'The row {below_row} is already filled and it should not')
        raise SystemExit
        

    
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