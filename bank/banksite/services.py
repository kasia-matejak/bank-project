from banksite.models import Account

def accounts_differ(sender: int, receiver: int):
    if sender == receiver:
        return False
    else:
        return True

# refactor - serializer takes validated data but you should implement the function CHANGING the validated data:
# - exchange integers to Account objects
# - import funds.available from selectors