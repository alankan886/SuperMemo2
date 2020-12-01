import json
import pytest

from supermemo2 import SMTwo


# test default convert on first visit
def test_first_visit_invalid_values():
    with pytest.warns(UserWarning) as record:
        sm_two = SMTwo(3, True, 999, 666, 777)

    assert len(record) == 3
    assert str(record[0].message) == "easiness automatically set to 2.5, easiness should be 2.5 for the first visit"
    assert str(record[1].message) == "interval automatically set to 1, interval should be 1 for the first visit"
    assert str(record[2].message) == "repetitions automatically set to 1, repetitions should be 1 for the first visit"
    assert sm_two.prev.easiness == 2.5
    assert sm_two.prev.interval == 1
    assert sm_two.prev.repetitions == 1


# test q >= 3 update attrs first visit
@pytest.mark.skip
def test_update_prev_attrs_first_visit():
    """
        After modifying the previous values, it should change the new values for some cases
    """
    sm_two = SMTwo(quality=3, first_visit=True)
    assert sm_two.easiness == 2.5
    assert sm_two.interval == 1
    assert sm_two.repetitions == 1

    # update repetitions to 1 should change interval to 1
    sm_two.prev.repetitions = 1
    assert sm_two.prev.json() == '{"easiness": 2.5, "interval": 0, "repetitions": 1}'
    assert sm_two.interval == 1


# test q >= 3 update attrs second visit
@pytest.mark.skip
def test_update_prev_attrs_second_visit():
    sm_two = SMTwo(quality=3, first_visit=False)

    # update repetitions to 2 should change interval to 6
    sm_two.prev.repetitions = 2
    assert sm_two.prev.json() == '{"easiness": 2.36, "interval": 1, "repetitions": 2}'
    assert sm_two.interval == 6

# test q >= 3 update attrs nth visit

# test q < 3 update attrs first visit

# test q < 3 update attrs second visit

# test q < 3 update attrs nth visit

# @pytest.mark.parametrize("first_visit, new_rep, new_inter", [(True, 1, 1), (False, 2, 6), (False, 3, 14)])
# def test_repeititons_setter(monkeypatch, first_visit, new_rep, new_inter):
#     sm_two = SMTwo(3, first_visit)
#     monkeypatch.setattr(sm_two, "interval", new_inter)
#     prev = Prev(sm_two, 3.0, 14, 4)
#     prev.repetitions = new_rep

#     assert sm_two.interval == new_inter
