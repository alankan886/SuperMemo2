from datetime import date

from .model import SMTwo


def first_review(quality, last_review=None):
    # Default arguments are evaluated only once - when the function is first parsed. We need it to reevaluate the date
    # each time this function is called.
    if last_review is None:
        last_review = date.today()

    smtwo = SMTwo()
    smtwo.calc(quality, 2.5, 1, 1, last_review)
    return smtwo


def modify(instance, quality=None, easiness=None, interval=None, repetitions=None, review_date=None):
    # specifically checking quality is None or not,
    # because quality can equal to 0, and that can get pick up instead.
    if not(quality is not None or easiness or interval or repetitions or review_date):
        message = "a new value is not provided for modification"
        raise ValueError(message)

    q = instance.quality
    ez = instance.prev.easiness
    inter = instance.prev.interval
    rep = instance.prev.repetitions
    rd = instance.prev.review_date

    if quality is not None:
        q = quality

    if easiness:
        ez = easiness

    if interval:
        inter = interval

    if repetitions:
        rep = repetitions

    if review_date is not None:
        rd = review_date

    instance.calc(q, ez, inter, rep, rd)
    return instance
