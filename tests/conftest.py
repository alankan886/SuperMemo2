import pytest

from supermemo2.sm_two import SMTwo


@pytest.fixture
def sm_two():
    return SMTwo(0)
