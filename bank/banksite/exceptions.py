from rest_framework.exceptions import APIException

class InsufficientFundsError(APIException):
    status_code = 400
    default_detail = "Insufficient funds"
    default_code = "bad_request"
        
class OwnTransferError(APIException):
    status_code = 400
    default_detail = "Accounts numbers provided are the same"
    default_code = "bad_request"

class UnexpectedTransferError(APIException):
    status_code = 500
    default_detail = "Unexpected error with transfering funds occurred"
    default_code = "internal_server-error"