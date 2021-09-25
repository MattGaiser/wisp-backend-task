import pytest

from api.api import special_math
from tests.constants import SPECIAL_MATH_TEST_CONSTANTS


def generate_special_math_arguments():
    test_values = SPECIAL_MATH_TEST_CONSTANTS

    return test_values


@pytest.mark.parametrize("test_input,expected", generate_special_math_arguments())
def test_special_math(test_input, expected):
    assert special_math(test_input) == expected
