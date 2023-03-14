from typing import Optional, TypedDict

from django.contrib.auth.models import BaseUserManager
from django.db.models import TextChoices


class UserType(TypedDict):
    name: str
    role: TextChoices
    password: str
    phone: Optional[str]
    email: str


class UserManager(BaseUserManager):
    def create(self, **kwargs: UserType):
        password = kwargs.pop("password")
        if email := kwargs.pop("email"):
            email = self.normalize_email(email).lower()
        user = self.model(
            email=email,
            **kwargs,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, name):
        return self.create(
            email=email,
            name=name,
            password=password,
            role=self.model.Roles.ADMIN,
            is_superuser=True,
        )
