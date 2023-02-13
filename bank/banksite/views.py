from .serializers import AccountSerializer, TransferSerializer
from .models import Account
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

class WelcomeMessage(APIView):
    def get(self, request):
        return Response({'message': 'Hello, this is the Bank'}, status=status.HTTP_200_OK)
    
class AccountInfo(APIView):
    def get_account_by_number(self, number):
        return Account.objects.get(number=number)
    
    def get(self, request, number):
        try:
            account=self.get_account_by_number(number)
            serializer = AccountSerializer(account)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'error': 'The account does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
class AccountCreation(APIView):
    def get(self, request):
        return Response({'message': 'Provide details to create an account'}, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class MakeTransfer(APIView):
    def get(self, request):
        return Response({'message': 'Make a transfer'}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TransferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        