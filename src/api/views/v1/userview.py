from django_mysqlpool import auto_close_db
from rest_framework import generics
from rest_framework import mixins
from rest_framework.status import HTTP_200_OK
from src.api.libraries.customresponse import CustomResponse
from src.api.libraries.loggingmixin import LoggingMixin
from src.common import UserLib
'''
{
    "email": "USER_EMAIL",
    "password": "User_Password"
}
'''

class UserView(LoggingMixin, generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin):

    @auto_close_db
    def post(self, request):
        details = request.data
        Response = UserLib(info=details).addUser
        return CustomResponse(message="File added to playlist successfully", payload=Response, code=HTTP_200_OK)

