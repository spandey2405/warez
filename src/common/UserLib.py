from src.models import User
import hashlib
import binascii, os
from src.constants import *
from django.core.exceptions import ValidationError

class UserLib():
    def __init__(self, **kwargs):
        self.arguments = kwargs
        self.info = self.arguments.get("info", False)

    def generate_salt(self):
        return binascii.hexlify(os.urandom(SALT_LENGTH/2)).decode()

    def password_hashing(self, password, salt=False):
        if not salt:
            salt = self.generate_salt()

        password_hash = str(password + salt)
        hash_library = hashlib.new(HASH_METHOD_USER_ADD)
        hash_library.update(password_hash)
        server_hash = hash_library.hexdigest()
        return salt, server_hash

    @property
    def addUser(self):

        if not self.info:
            raise ValidationError("Missing user Information")
        try:
            self.info["password"], self.info["salt"] = self.password_hashing(
                self.info["password"]
            )
            User.objects.create(**self.info)
            response = "User Created"
        except Exception as e:
            response = "Error Creating User : {}".format(e)
        return response
