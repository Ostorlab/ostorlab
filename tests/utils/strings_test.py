"""Unit test for strings utils module."""
import pytest

from ostorlab.utils import strings


# pylint: disable=W0631
def testRandomString_whenLengthIsValid_returnsARandomStringOfSpecifiedSize():
    """Tests if a proper random string is generated."""
    generated = strings.random_string(6)

    assert isinstance(generated, str)
    assert len(generated) == 6


def testRandomString_whenLengthIsInvalid_raisesAnException():
    """Tests if an exception is raised when a incorrect length value is provided."""
    with pytest.raises(ValueError):
        strings.random_string(0)
