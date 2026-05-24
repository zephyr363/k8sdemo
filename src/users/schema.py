from ninja import ModelSchema
from users.models import User

class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class UserCreateSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["username", "email", "password"]