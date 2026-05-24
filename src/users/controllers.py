from ninja_extra import api_controller, route
from ninja_extra.exceptions import NotFound, ValidationError
from .models import User
from .schema import UserSchema


@api_controller("/users", tags=["Users"])
class UserController:
    @route.get("/", response=list[UserSchema])
    def list_users(self):
        return User.objects.all()

    @route.post("/create", response=UserSchema)
    def create_user(self, user: UserSchema):
        try:
            return User.objects.create_user(**user.dict())
        except Exception as e:
            raise ValidationError(str(e))

    @route.get("/{user_id}", response=UserSchema)
    def get_user(self, user_id: int):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound()
