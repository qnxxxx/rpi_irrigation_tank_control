from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        userModel = get_user_model()
        if username is None:
            username = kwargs.get(userModel.USERNAME_FIELD)

        try:
            case_insensitive_username_field = '{}__iexact'.format(userModel.USERNAME_FIELD)
            user = userModel._default_manager.get(**{case_insensitive_username_field: username})
        except userModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            userModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
