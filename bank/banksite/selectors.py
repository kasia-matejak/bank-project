from banksite.models import Account

def funds_available(sender, ammount):
    sender = Account.objects.get(number=sender)
    if sender.status > ammount:
        return True
    else:
        return False