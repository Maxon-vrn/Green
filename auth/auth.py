from fastapi_users import fastapi_users
from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

#CookieTransport - болле подробно о параметрах смотри в документации
cookie_transport = CookieTransport(
    cookie_max_age=3600)  # дополнительные параметры в CookieTransport(cookie_name='bonds',cookie_max_age=3600)

#JSON Web Token (JWT) is an internet standard for creating access tokens based on JSON. They don't need to be stored in a database: the data is self-contained inside and cryptographically signed.
SECRET = "SECRET"  # - SECRET - задать строчку и храните его в .env и в файле config.py  его импортировать


def get_jwt_strategy() -> JWTStrategy:  #функция кодирования и декодирования при помощи токена
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

# Получаем текущего аутентифицированного пользователя
#current_user = fastapi_users.current_user() хз что это