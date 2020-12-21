import pytest

from supermemo2.model import SMTwo


@pytest.fixture
def smtwo():
    return SMTwo()
