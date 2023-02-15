from rest_framework import serializers
from banksite.models import Account, Transfer
from banksite.selectors import funds_available


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["number", "name", "status"]

    def create(self, validated_data):
        return Account.objects.create(**validated_data)


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ["sender", "receiver", "ammount", "description"]

    def get_account_by_number(self, number):
        return Account.objects.get(number=number)

    def create(self, validated_data):
        sender_account = self.get_account_by_number(number=validated_data["sender"])
        receiver_account = self.get_account_by_number(number=validated_data["receiver"])
        if funds_available(sender_account, validated_data['ammount']):
            return Transfer.objects.create(
                sender=sender_account,
                receiver=receiver_account,
                ammount=validated_data["ammount"],
                description=validated_data["description"]
            )
