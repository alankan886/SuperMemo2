import pytest

from supermemo2.models import Prev


@pytest.fixture
def mock_prev():
    class MockSMTwo:
        pass

    return Prev(MockSMTwo, 3.0, 14, 4)
