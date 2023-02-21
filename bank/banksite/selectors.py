from banksite.models import Account
from .exceptions import InsufficientFundsError

def funds_available(sender: Account, ammount):
    if sender.status > ammount:
        return
    else:
        raise InsufficientFundsError