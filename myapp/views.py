from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OPT_Party, OPT_Address

@api_view(['GET'])
def get_clients(request):
    clients = OPT_Party.objects.all().values('PTY_ID', 'PTY_FirstName', 'PTY_LastName', 'PTY_Phone', 'PTY_SSN')
    
    client_data = []
    for client in clients:
        addresses = OPT_Address.objects.filter(Add_PartyID=client['PTY_ID']).values('Add_Line1', 'Add_City', 'Add_State__Stt_Code', 'Add_Zip')
        client['addresses'] = list(addresses)
        client_data.append(client)
    
    return Response({'clients': client_data})
