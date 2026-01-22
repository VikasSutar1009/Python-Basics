import pytest

from services.auth_service import generate_token

def test_token_generation():
    token = generate_token(1)
    assert token is not None