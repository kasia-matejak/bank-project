from rest_framework import serializers
from banksite.models import Account, Transfer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["number", "name", "status"]

    def create(self, validated_data):
        return Account.objects.create(**validated_data)


class TransferSerializer(serializers.Serializer):
    class Meta:
        model = Transfer
        fields = ["sender", "receiver", "ammount", "description"]
        depth = 1

    def get_account_by_number(self, account_number):
        return Account.objects.get(number=account_number)

    def create(self, validated_data):
        sender_account = self.get_account_by_number(number=validated_data["sender"])
        receiver_account = self.get_account_by_number(number=validated_data["receiver"])
        return Transfer.objects.create(
            sender=sender_account,
            receiver=receiver_account,
            ammount=validated_data["ammount"],
            description=validated_data["description"],
        )
