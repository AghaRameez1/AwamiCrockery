import re
from django.core.exceptions import ValidationError


def is_ascii(s):
    """
    Internal function to check for ASCII in a string
    :param s:
    :return:
    """
    return all(ord(c) < 128 for c in s)

def ascii_validator(value):
    is_clean = is_ascii(value)
    if not is_clean:
        raise ValidationError("Special characters are not allowed.")
    return value

def numeric_validator(value):
    try:
        re.match('^[0-9]+$', value).group(0)
    except:
        raise ValidationError("Only numeric values allowed")
    return value