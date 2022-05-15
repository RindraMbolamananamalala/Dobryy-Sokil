import os
import tempfile

import pytest


@pytest.fixture(autouse=True)
def database():
    _, file_name = tempfile.mkstemp()
    os.environ["DATABASE_NAME"] = file_name


def input_value():
    input = 39
    return input


@pytest.fixture(scope="class", name="input_value", autouse=True)
def input_value_indirect():
    return input_value()
