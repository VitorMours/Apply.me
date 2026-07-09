import importlib

import pydantic
import pytest
from pydantic import BaseModel


class TestAuthSchemas:
    def test_if_can_import_schemas(self) -> None:
        try:
            from app.schemas.auth_schemas import (
                Credentials,
                LoginCredentials,
                ReceiveToken,
                SigninCredentials,
            )

            assert Credentials is not None
            assert LoginCredentials is not None
            assert SigninCredentials is not None
            assert ReceiveToken is not None
        except ImportError as exc:
            raise ImportError("Was not possible to import the auth schemas") from exc

    def test_if_auth_schemas_are_pydantic_models(self) -> None:
        module = importlib.import_module("app.schemas.auth_schemas")

        assert issubclass(module.Credentials, BaseModel)
        assert issubclass(module.LoginCredentials, module.Credentials)
        assert issubclass(module.SigninCredentials, module.Credentials)
        assert issubclass(module.ReceiveToken, BaseModel)

    def test_if_credentials_schema_have_expected_fields(self) -> None:
        module = importlib.import_module("app.schemas.auth_schemas")
        fields = module.Credentials.model_fields

        assert "email" in fields
        assert "password" in fields

    def test_if_signin_schema_have_expected_fields(self) -> None:
        module = importlib.import_module("app.schemas.auth_schemas")
        fields = module.SigninCredentials.model_fields

        assert "name" in fields
        assert "email" in fields
        assert "password" in fields

    def test_if_receive_token_schema_have_expected_fields(self) -> None:
        module = importlib.import_module("app.schemas.auth_schemas")
        fields = module.ReceiveToken.model_fields

        assert "access_token" in fields
        assert "token_type" in fields
        assert "user_id" in fields

    def test_if_credentials_validate_data(self) -> None:
        module = importlib.import_module("app.schemas.auth_schemas")

        credentials = module.Credentials(email="user@email.com", password="secret123")

        assert credentials.email == "user@email.com"
        assert credentials.password == "secret123"

    def test_if_signin_credentials_validate_data(self) -> None:
        module = importlib.import_module("app.schemas.auth_schemas")

        credentials = module.SigninCredentials(
            name="João",
            email="user@email.com",
            password="secret123",
        )

        assert credentials.name == "João"
        assert credentials.email == "user@email.com"
        assert credentials.password == "secret123"

    def test_if_receive_token_validate_data(self) -> None:
        module = importlib.import_module("app.schemas.auth_schemas")

        token = module.ReceiveToken(
            access_token="abc123",
            token_type="bearer",
            user_id="42",
        )

        assert token.access_token == "abc123"
        assert token.token_type == "bearer"
        assert token.user_id == "42"

    def test_auth_schemas_raise_validation_errors_for_invalid_types(self) -> None:
        module = importlib.import_module("app.schemas.auth_schemas")

        with pytest.raises(pydantic.ValidationError):
            module.Credentials(email=123, password="secret123")

        with pytest.raises(pydantic.ValidationError):
            module.SigninCredentials(name=123, email="user@email.com", password="secret123")

        with pytest.raises(pydantic.ValidationError):
            module.ReceiveToken(access_token=123, token_type="bearer", user_id="42")