from .serializers import UserSerializer


def auth_payload_handler(token, user=None, request=None):

    return {
        'token': token,
        'user': UserSerializer(user).data
    }
