import json

import pytest

from supermemo2.models import Prev


def test_easiness_getter(mock_prev):
    assert mock_prev.easiness == 3.0


def test_interval_getter(mock_prev):
    assert mock_prev.interval == 14


def test_repeititons_getter(mock_prev):
    assert mock_prev.repetitions == 4


def test_json(mock_prev):
    assert mock_prev.json() == json.dumps({"easiness": 3.0, "interval": 14, "repetitions": 4})
