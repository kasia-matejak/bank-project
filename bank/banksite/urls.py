# from django.urls import path
from .views import AccountInfo, AccountCreation, WelcomeMessage, MakeTransfer
from django.urls import path


urlpatterns = [
    path('', WelcomeMessage.as_view()),
    path('account/', AccountCreation.as_view()),
    path('account/<int:number>/', AccountInfo.as_view()),
    path('transfer/', MakeTransfer.as_view())
]