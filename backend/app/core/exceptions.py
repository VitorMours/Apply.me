class AppException(Exception):
    """Exceção base da aplicação"""
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class UserNotFoundException(AppException):
    def __init__(self, identifier: str | int):
        self.identifier = identifier
        super().__init__(f"Usuário '{identifier}' não encontrado")