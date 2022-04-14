from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from ..authentication.firebase import FirebaseAuthentication

@api_view(['GET', ])
@authentication_classes([FirebaseAuthentication])
def index(request):
    print(request.user.email)
    return Response({"message": "Hello, World"})
