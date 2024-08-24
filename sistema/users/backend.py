from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

class EmailBackend(BaseBackend):
    """
    Backend de autenticação personalizado que permite que os usuários façam login usando seu e-mail e senha.
    """
    def authenticate(self, request, email=None, password=None, **kwargs):
        User = get_user_model()
        try:
            # Tenta encontrar o usuário pelo email
            user = User.objects.get(email=email)
            # Verifica se a senha é válida
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None