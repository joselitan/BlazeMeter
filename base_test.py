import pytest


@pytest.mark.usefixtures("driver_init")
class BaseTest:
    print("basetest")
    pass
