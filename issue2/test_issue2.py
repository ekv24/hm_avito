from morse import decode
import pytest


@pytest.mark.parametrize(
    "morse_code, message",
    [
        (".---- ..--- ...--", "123"),
        (".... . .-.. .-.. --- -....- .-- --- .-. .-.. -..", "HELLO-WORLD"),
        ("... --- ...", "SOS"),
    ],
)
def test_decode(morse_code, message):
    assert decode(morse_code) == message
