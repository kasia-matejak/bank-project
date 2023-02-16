from banksite.models import Account
from .exceptions import InsufficientFundsError

def funds_available(sender: int, ammount):
    sender = Account.objects.get(number=sender)
    if sender.status > ammount:
        return
    else:
        raise InsufficientFundsError