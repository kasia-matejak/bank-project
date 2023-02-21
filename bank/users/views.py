from rest_framework.views import APIView
from users.serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from users.models import User
from  django.contrib.auth.hashers import check_password
import datetime
import jwt

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self, request):
        name = request.data['name']
        password = request.data['password']
        
        user = User.objects.get(name=name)
        if not user:
            raise AuthenticationFailed('User not found')
        
        if not check_password(password, user.password):
            raise AuthenticationFailed('Incorrect password')
        
        payload = {'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60), 'iat': datetime.datetime.utcnow()}
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        res = Response()
        res.data = {'jwt': token}
        res.set_cookie(key='jwt', value=token, httponly=True)
        
        return res
    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated. No token was passed')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except:
            raise AuthenticationFailed('Unauthenticated')
        user = User.objects.get(id=payload['id'])
        
        serializer = UserSerializer(user)   
        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {'message': 'Logged out successfuly'}
        
        return response