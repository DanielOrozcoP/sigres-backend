from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from control_acceso_app.auth.serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'El registro del usuario fue exitoso'
            data['username'] = account.username
            data['email'] = account.email
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            data = serializer.errors
        
        return Response(data)