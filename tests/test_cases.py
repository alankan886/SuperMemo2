from datetime import datetime 


attributes = "quality, interval, repetitions, easiness, first_visit, last_review"

anything = [
    (0, 60, 7, 1.5, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()),
    (1, 30, 4, 1.6, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()),
    (2, 15, 3, 1.7, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()),
    (0, 60, 7, 1.5, False, "2020-07-13"),
    (1, 30, 4, 1.6, False, "2020-07-13"),
    (2, 15, 3, 1.7, False, "2020-07-13"),
    (1, 0, 1, 2.5, True, datetime.strptime("2020-07-13", "%Y-%m-%d").date()),
    (1, 0, 1, 2.5, True, "2020-07-13"),
    (3, 31, 6, 1.3, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()),
    (0, 24, 4, 1.4, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()),
    (3, 12, 5, 1.4, False, "2020-07-13")
]

quality_less_than_three_nth_visit = [
    [0, 60, 7, 1.5, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [1, 30, 4, 1.6, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [2, 15, 3, 1.7, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [0, 60, 7, 1.5, False, "2020-07-13"],
    [1, 30, 4, 1.6, False, "2020-07-13"],
    [2, 15, 3, 1.7, False, "2020-07-13"],
    [1, 0, 1, 2.5, True, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [1, 0, 1, 2.5, True, "2020-07-13"]
]

quality_three_nth_visit_break_easiness_lowerbound = [
    [3, 31, 6, 1.3, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [3, 24, 4, 1.4, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [3, 12, 5, 1.4, False, "2020-07-13"]
]

first_visit = [
    [3, 0, 1, 2.5, True, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [4, 0, 1, 2.5, True, "2020-07-13"]
]

repetitions_equals_two = [
    [3, 1, 2, 2.5, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [4, 1, 2, 2.5, False, "2020-07-13"]
]

first_visit_input_value_error_handler = [
    (0, 1, 1, 2.5, True, "2020-07-14"),
    (0, -1, 1, 2.5, True, "2020-07-14"),
    (1, 0, 0, 2.5, True, "2020-07-14"),
    (1, 0, 2, 2.5, True, "2020-07-14"),
    (1, 0, 1, 2.4, True, "2020-07-14"),
    (1, 0, 1, 2.6, True, "2020-07-14"),
    (-1, 0, 1, 2.5, True, "2020-07-14"),
    (6, 0, 1, 2.5, True, "2020-07-14"),
    (5, 0, 1, 2.5, True, ""),
    (3, 0, 1, 2.5, True, "abcabc"),
    (3, 0, 1, 2.5, True, "06-15-2020"),
    (123, 123, 123, 123, True, "2020-07-14")
]

nth_visit_input_value_error_handler = [
    (2, 30, 4, 1.0, False, "2020-05-06")
]

input_type_error_handler = [
    ("abc", 0, 1, 2.5, True, "2020-07-14"),
    (1, "cba", 1, 2.5, True, "2020-07-14"),
    (2, 0, "abc", 2.5, True, "2020-07-14"),
    (3, 0, 1, "efg", True, "2020-07-14"),
    (3, 0, 1, 2.5, "abc", "2020-07-14"),
    (4, 0, 1, 2.5, True, 123),
    ("abc", "def", "hij", "lmn", "opr", "xyz")
]