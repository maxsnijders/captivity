"""

Captivity main file

"""


import warnings


def warning_mode():
    global flag_issue
    flag_issue = raise_warning


def exception_mode():
    global flag_issue
    flag_issue = raise_exception


class CaptivityException(Exception):
    pass


class CaptivityWarning(Warning):
    pass


def raise_exception(message: str):
    raise CaptivityException(message)


def raise_warning(message: str):
    warnings.warn(message, CaptivityWarning)


flag_issue = raise_exception

from captivity import merge
from captivity import concat
