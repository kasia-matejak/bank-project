from rest_framework import serializers
from banksite.models import Account
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .exceptions import AccountDoesNotExistError
from banksite.services import get_account_by_number, create_transfer

class WelcomeMessage(APIView):
    def get(self, request):
        return Response({'message': 'Hello, this is the Bank'}, status=status.HTTP_200_OK)
    
class AccountCreation(APIView):
    class AccountSerializer(serializers.ModelSerializer):
        class Meta:
            model = Account
            fields = ["number", "name", "status"]

        def create(self, validated_data):
            return Account.objects.create(**validated_data)
            
    def get(self, request):
        return Response({'message': 'Provide details to create an account'}, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = self.AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class AccountInfo(APIView):
    def get(self, request, number):
        try:
            account = get_account_by_number(number=number)
            serializer = AccountCreation.AccountSerializer(account)
            return Response(serializer.data)
        except AccountDoesNotExistError:
            return Response({'error': 'The account does not exist'}, status=status.HTTP_404_NOT_FOUND)

class MakeTransfer(APIView):
    class TransferSerializer(serializers.Serializer):
        sender = serializers.IntegerField()
        receiver = serializers.IntegerField()
        ammount = serializers.IntegerField()
        description = serializers.CharField(max_length=100)
        
    def get(self, request):
        return Response({'message': 'Make a transfer'}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.TransferSerializer(data=request.data)
        if serializer.is_valid():
            create_transfer(serializer.data)
            return Response({'message': 'successfuly transfered', 'detail': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)