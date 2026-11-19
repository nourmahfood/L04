import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
return grade > 5


# bug report 2
def is_valid_password(password):
    """At least 8 characters and at least one digit"""
    return len(password) > 8 and any(c.isdigit() for c in password)


# bug report 3
def clamp(x, low, high):
    """x, limited to the range from low to high"""
    return max(low, min(x, low))
