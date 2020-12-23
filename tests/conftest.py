from datetime import date

import pytest

from supermemo2.model import SMTwo


@pytest.fixture
def empty_smtwo():
    return SMTwo()


@pytest.fixture
def smtwo_after_calc():
    smtwo = SMTwo()
    smtwo.calc(3, 2.5, 1, 1, date.today())
    return smtwo
