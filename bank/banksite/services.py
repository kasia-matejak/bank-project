from banksite.models import Account, Transfer
from .selectors import funds_available
from django.core.exceptions import ObjectDoesNotExist
from .exceptions import *

def get_account_by_number(number: int):
    try:
        return Account.objects.get(number=number)
    except ObjectDoesNotExist:
        raise AccountDoesNotExistError

def create_transfer(validated_data) -> Transfer:
    sender = get_account_by_number(number=validated_data['sender'])
    receiver = get_account_by_number(number=validated_data['receiver'])
    ammount = validated_data['ammount']
    description = validated_data['description']
    try:
        make_transfer(sender, receiver, ammount)
        obj = Transfer(sender=sender, receiver=receiver, ammount=ammount, description=description)
        obj.save()
        return obj
    except (Exception, OwnTransferError, InsufficientFundsError, UnexpectedTransferError):
        raise

def accounts_differ(sender: Account, receiver: Account):
    if sender.number != receiver.number:
        return
    else:
        raise OwnTransferError

def move_money(sender: Account, receiver: Account, ammount: int):
    try:
        sender.status = sender.status - ammount
        receiver.status = receiver.status + ammount
        sender.save()
        receiver.save()
    except:
        raise UnexpectedTransferError

def make_transfer(sender: Account, receiver: Account, ammount: int):
    try:
        accounts_differ(sender, receiver)
        funds_available(sender, ammount)
        move_money(sender, receiver, ammount)
    except (OwnTransferError, InsufficientFundsError, UnexpectedTransferError):
        raise