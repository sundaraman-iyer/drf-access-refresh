from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework.response import Response 
from rest_framework.views import APIView


from .authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token
from .serializers import UserSerializer
from .models import User
# Create your views here.

#Registering a new user
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginAPIView(APIView):
    def post(self, request):
        user = User.objects.filter(email = request.data['email']).first()

        if not user: # if user not found
            raise APIException("Invalid Credentials")
        
        if not user.check_password(request.data['password']):
            raise APIException("Invalid Credentials!!")
        
        access_token = create_access_token(user.id)  # returned in respose to the serializer
        refresh_token = create_refresh_token(user.id) # this will be returned as a cookie

        response = Response()

        response.set_cookie(key='refreshToken', value=refresh_token, httponly=True) # the backend will only get the cookie, but the frontend will not be access it

        response.data = {

            'token': access_token
        }
        return response
    
class UserAPIView(APIView): #getting the users
    def get(self, request):
        #step 1: Get the access token from header into the bearer and payload
        auth =  get_authorization_header(request).split()
    
        #issue is here, it is not going into the if condition
        #it is not picking up authorization from the header
        
        # #step 2: checking the len of auth i.e does it have bearer and token
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = User.objects.filter(pk=id).first()

            return Response(UserSerializer(user).data) # similar to line 15-18, here done in 1 line
        
        raise AuthenticationFailed('unauthicated')