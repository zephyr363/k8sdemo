from ninja_extra import api_controller
from ninja_extra.exceptions import NotFound, ValidationError
from .models import User
from .schema import UserSchema


@api_controller("/users", tags=["Users"])
class UserController:
    def list_users(self) -> list[UserSchema]:
        return [UserSchema.from_orm(user) for user in User.objects.all()]

    def get_user(self, user_id: int) -> UserSchema:
        try:
            user = User.objects.get(id=user_id)
            return UserSchema.from_orm(user)
        except User.DoesNotExist:
            raise NotFound()

    def create_user(self, user: UserSchema) -> UserSchema:
        try:
            user_obj = User.objects.create_user(**user.dict())
        except Exception as e:
            raise ValidationError(str(e))
        return UserSchema.from_orm(user_obj)

    def update_user(self, user_id: int, user: UserSchema) -> UserSchema:
        try:
            user_obj = User.objects.get(id=user_id)
            for attr, value in user.dict().items():
                setattr(user_obj, attr, value)
            user_obj.save()
            return UserSchema.from_orm(user_obj)
        except User.DoesNotExist:
            raise NotFound()
        except Exception as e:
            raise ValidationError(str(e))
